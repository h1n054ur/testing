import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from app.models.country_data import COUNTRY_DATA

class TwilioGateway:
    """
    Abstraction over Twilio SDK for unified access.
    Handles all Twilio API interactions and HTTP requests for number search.
    """
    def __init__(self, account_sid: str, auth_token: str):
        """Initialize TwilioGateway with credentials."""
        if not account_sid or not auth_token:
            raise ValueError("Both account_sid and auth_token are required")
        self._account_sid = account_sid
        self._auth_token = auth_token
        try:
            self._client = Client(account_sid, auth_token)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Twilio client: {str(e)}")

    def search_available_numbers(self, country_code: str, number_type: str = None,
                               region: str = None, area_code: str = None, pattern: str = None,
                               page: int = 1, limit: int = 20):
        """
        Search for available numbers using direct HTTP requests.
        Returns list of dicts with number details.

        Args:
            country_code: Country code (e.g., 'US')
            number_type: Type of number ('local', 'mobile', 'tollfree')
            region: Optional region name
            area_code: Optional area code to search in
            pattern: Optional pattern to search for
            page: Page number for pagination
            limit: Numbers per page
        """
        # Map number types to API paths
        type_map = {
            "local": "Local",
            "mobile": "Mobile",
            "tollfree": "TollFree"
        }
        number_type = type_map.get(number_type, "Local")
        
        # Build URL
        base_url = f"https://api.twilio.com/2010-04-01/Accounts/{self._account_sid}/AvailablePhoneNumbers/{country_code}/{number_type}.json"

        # Build query parameters
        params = {
            "PageSize": limit,
            "Page": page
        }

        # Add region filter if provided
        if region:
            # For GB, use exact region name from country data
            if country_code == "GB":
                # Get exact region name from country data to ensure correct casing
                for region_name in COUNTRY_DATA[country_code]["regions"].keys():
                    if region_name.lower() == region.lower():
                        params["InRegion"] = region_name
                        break
            # For US, use state name
            elif country_code == "US":
                # First try exact match
                if region in COUNTRY_DATA[country_code]["regions"]:
                    params["InRegion"] = region
                else:
                    # Try case-insensitive match
                    for state_name in COUNTRY_DATA[country_code]["regions"].keys():
                        if state_name.lower() == region.lower():
                            params["InRegion"] = state_name
                            break
            # For CA, use region code
            elif country_code == "CA":
                region_code = COUNTRY_DATA[country_code]["regions"].get(region, {}).get("code")
                if region_code:
                    params["InRegion"] = region_code

        # Add area code filter for US/CA
        if area_code:
            if country_code in ["US", "CA"]:
                params["AreaCode"] = area_code

        # Add pattern search
        if pattern:
            # For US/CA, if pattern is 3 digits, try area code first
            if country_code in ["US", "CA"] and len(pattern) == 3 and pattern.isdigit():
                # Check if it's a valid area code
                area_codes = set()
                for region_data in COUNTRY_DATA[country_code]["regions"].values():
                    area_codes.update(region_data["area_codes"])
                
                if int(pattern) in area_codes:
                    params["AreaCode"] = pattern
                else:
                    # Not a valid area code, treat as pattern search
                    params["Contains"] = f"*{pattern}*"
            else:
                # For pattern search, we need to add wildcards for better matching
                if pattern.isdigit():
                    if len(pattern) <= 7:  # Don't use wildcards for full numbers
                        params["Contains"] = f"*{pattern}*"
                    else:
                        params["Contains"] = pattern

        try:
            # Make HTTP request
            response = requests.get(
                base_url,
                params=params,
                auth=(self._account_sid, self._auth_token)
            )
            # Debug the actual URL being called
            print(f"DEBUG - Request URL: {response.request.url}")
            print(f"DEBUG - Request Headers: {response.request.headers}")
            response.raise_for_status()
            data = response.json()

            # Extract and format numbers
            numbers = data.get("available_phone_numbers", [])
            
            # Format numbers with proper region/state mapping
            formatted_numbers = []
            for num in numbers:
                api_region = num.get("region", "")
                api_locality = num.get("locality", "")
                
                # For US/CA, use region name from country data
                if country_code in ["US", "CA"]:
                    # Find region name by matching region code
                    region_name = None
                    for name, data in COUNTRY_DATA[country_code]["regions"].items():
                        if data.get("code") == api_region:
                            region_name = name
                            break
                    formatted_numbers.append({
                        "number": num["phone_number"],
                        "friendly_name": num.get("friendly_name", ""),
                        "city": api_locality,
                        "state": region_name or api_region,  # Use matched name or fallback to code
                        "type": number_type.lower(),
                        "capabilities": {
                            "voice": num.get("capabilities", {}).get("voice", False),
                            "sms": num.get("capabilities", {}).get("sms", False),
                            "mms": num.get("capabilities", {}).get("mms", False)
                        },
                        "price": num.get("monthly_fee", "0.00")
                    })
                # For GB/AU, use region name directly
                else:
                    formatted_numbers.append({
                        "number": num["phone_number"],
                        "friendly_name": num.get("friendly_name", ""),
                        "city": api_locality,
                        "state": api_region,  # Use region directly
                        "type": number_type.lower(),
                        "capabilities": {
                            "voice": num.get("capabilities", {}).get("voice", False),
                            "sms": num.get("capabilities", {}).get("sms", False),
                            "mms": num.get("capabilities", {}).get("mms", False)
                        },
                        "price": num.get("monthly_fee", "0.00")
                    })
            
            return {
                "success": True,
                "numbers": formatted_numbers
            }
        except requests.RequestException as e:
            print(f"Error searching numbers: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "numbers": []
            }

    def purchase_number(self, phone_number: str):
        """Purchase a phone number using Twilio SDK."""
        try:
            number = self._client.incoming_phone_numbers.create(
                phone_number=phone_number
            )
            return {
                "success": True,
                "number": number.phone_number,
                "sid": number.sid
            }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    def release_number(self, phone_number: str):
        """Release a phone number using Twilio SDK."""
        try:
            numbers = self._client.incoming_phone_numbers.list(
                phone_number=phone_number
            )
            if not numbers:
                return {
                    "success": False,
                    "error": "Number not found"
                }
            numbers[0].delete()
            return {
                "success": True,
                "message": f"Released {phone_number}"
            }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    def list_active_numbers(self):
        """List all active numbers using Twilio SDK."""
        try:
            numbers = self._client.incoming_phone_numbers.list()
            return {
                "success": True,
                "numbers": [
                    {
                        "number": num.phone_number,
                        "friendly_name": num.friendly_name,
                        "sid": num.sid,
                        "capabilities": {
                            "voice": num.capabilities.get("voice", False),
                            "sms": num.capabilities.get("sms", False),
                            "mms": num.capabilities.get("mms", False)
                        }
                    }
                    for num in numbers
                ]
            }
        except TwilioRestException as e:
            print(f"Error listing active numbers: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "numbers": []
            }

    def send_sms(self, from_number: str, to_number: str, message: str):
        """Send SMS using Twilio SDK."""
        try:
            message = self._client.messages.create(
                from_=from_number,
                to=to_number,
                body=message
            )
            return {
                "success": True,
                "sid": message.sid,
                "status": message.status
            }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    def make_call(self, from_number: str, to_number: str, url: str = None,
                  twiml: str = None):
        """Make a call using Twilio SDK."""
        try:
            call_params = {
                "from_": from_number,
                "to": to_number
            }
            if url:
                call_params["url"] = url
            elif twiml:
                call_params["twiml"] = twiml
            else:
                return {
                    "success": False,
                    "error": "Either url or twiml must be provided"
                }

            call = self._client.calls.create(**call_params)
            return {
                "success": True,
                "sid": call.sid,
                "status": call.status
            }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_messaging_logs(self, phone_number: str = None):
        """Get messaging logs using Twilio SDK."""
        try:
            params = {}
            if phone_number:
                params["from_"] = phone_number

            messages = self._client.messages.list(**params)
            return {
                "success": True,
                "messages": [
                    {
                        "sid": msg.sid,
                        "from": getattr(msg, 'from_formatted', None) or getattr(msg, 'from_', None),  # Try formatted first
                        "to": getattr(msg, 'to_formatted', None) or msg.to,
                        "body": msg.body,
                        "status": msg.status,
                        "direction": "Outbound" if msg.direction in ["outbound-api", "outbound", "trunking-originating"] else "Inbound" if msg.direction in ["inbound", "trunking-terminating"] else msg.direction,
                        "date_sent": msg.date_sent,
                        "price": msg.price or 0  # Handle None price
                    }
                    for msg in messages
                ]
            }
        except TwilioRestException as e:
            print(f"Error getting messaging logs: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "messages": []
            }

    def get_call_logs(self, phone_number: str = None):
        """Get call logs using Twilio SDK."""
        try:
            params = {}
            if phone_number:
                params["from_"] = phone_number

            calls = self._client.calls.list(**params)
            # Debug: Print first call details
            if calls:
                first_call = calls[0]
                print(f"DEBUG Call Info:")
                print(f"  direction: {first_call.direction}")
                print(f"  from_: {getattr(first_call, 'from_', None)}")
                print(f"  from_formatted: {getattr(first_call, 'from_formatted', None)}")
                print(f"  to: {first_call.to}")
                print(f"  to_formatted: {first_call.to_formatted}")
                print(f"  trunk_sid: {first_call.trunk_sid}")
                print(f"  forwarded_from: {first_call.forwarded_from}")
                print(f"  direction type: {type(first_call.direction)}")
                print(f"  All attributes: {dir(first_call)}")

            return {
                "success": True,
                "calls": [
                    {
                        "sid": call.sid,
                        "from": getattr(call, 'from_formatted', None) or getattr(call, 'from_', None),  # Try formatted first
                        "to": getattr(call, 'to_formatted', None) or call.to,
                        "status": call.status,
                        "direction": "Outbound" if call.direction in ["outbound-api", "outbound", "trunking-originating"] else "Inbound" if call.direction in ["inbound", "trunking-terminating"] else call.direction,
                        "duration": call.duration,
                        "start_time": call.start_time,
                        "price": call.price or 0  # Handle None price
                    }
                    for call in calls
                ]
            }
        except TwilioRestException as e:
            print(f"Error getting call logs: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "calls": []
            }

    def get_number_config(self, phone_number: str):
        """Get number configuration using Twilio SDK."""
        try:
            numbers = self._client.incoming_phone_numbers.list(
                phone_number=phone_number
            )
            if not numbers:
                return {
                    "success": False,
                    "error": "Number not found"
                }
            number = numbers[0]
            return {
                "success": True,
                "config": {
                    "friendly_name": number.friendly_name,
                    "voice_url": number.voice_url,
                    "voice_method": number.voice_method,
                    "sms_url": number.sms_url,
                    "sms_method": number.sms_method,
                    "status_callback": number.status_callback,
                    "capabilities": number.capabilities
                }
            }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    def set_number_config(self, phone_number: str, config: dict):
        """Update number configuration using Twilio SDK."""
        try:
            numbers = self._client.incoming_phone_numbers.list(
                phone_number=phone_number
            )
            if not numbers:
                return {
                    "success": False,
                    "error": "Number not found"
                }
            number = numbers[0]
            number.update(**config)
            return {
                "success": True,
                "message": "Configuration updated successfully"
            }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    def get_account_logs(self, log_type: str = None):
        """Get account-wide logs using Twilio SDK."""
        try:
            if log_type == "messages":
                return self.get_messaging_logs()
            elif log_type == "calls":
                return self.get_call_logs()
            else:
                # Return both types of logs
                return {
                    "messages": self.get_messaging_logs(),
                    "calls": self.get_call_logs()
                }
        except TwilioRestException as e:
            return {
                "success": False,
                "error": str(e)
            }
