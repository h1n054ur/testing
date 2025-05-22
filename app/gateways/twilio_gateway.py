import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

class TwilioGateway:
    """
    Abstraction over Twilio SDK for unified access.
    Handles all Twilio API interactions and HTTP requests for number search.
    """
    def __init__(self, account_sid: str, auth_token: str):
        """Initialize TwilioGateway with credentials."""
        self._account_sid = account_sid
        self._auth_token = auth_token
        self._client = Client(account_sid, auth_token)

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

        # Add region filter for US numbers
        if region and country_code == "US":
            # Map region name to state code
            state_map = {
                "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
                "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
                "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
                "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
                "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
                "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
                "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
                "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
                "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
                "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
                "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
                "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
                "Wisconsin": "WI", "Wyoming": "WY", "Washington DC": "DC"
            }
            state_code = state_map.get(region)
            if state_code:
                params["InRegion"] = state_code

        # Add area code filter
        if area_code:
            params["AreaCode"] = area_code

        # Add pattern search - always use Contains
        if pattern:
            params["Contains"] = pattern

        try:
            # Make HTTP request
            response = requests.get(
                base_url,
                params=params,
                auth=(self._account_sid, self._auth_token)
            )
            response.raise_for_status()
            data = response.json()

            # Extract and format numbers
            numbers = data.get("available_phone_numbers", [])
            return [
                {
                    "number": num["phone_number"],
                    "friendly_name": num.get("friendly_name", ""),
                    "city": num.get("locality", ""),
                    "state": (
                        num.get("region", "") if country_code in ["US", "CA", "AU"] 
                        else num.get("region", "") if country_code == "GB"
                        else num.get("administrative_area", "")
                    ),
                    "type": number_type.lower(),
                    "capabilities": {
                        "voice": num.get("capabilities", {}).get("voice", False),
                        "sms": num.get("capabilities", {}).get("sms", False),
                        "mms": num.get("capabilities", {}).get("mms", False)
                    },
                    "price": num.get("monthly_fee", "0.00")
                }
                for num in numbers
            ]
        except requests.RequestException as e:
            print(f"Error searching numbers: {str(e)}")
            return []

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
            return [
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
        except TwilioRestException as e:
            return []

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
            return [
                {
                    "sid": msg.sid,
                    "from": getattr(msg, 'from_', None),  # Use from_ for outbound messages
                    "to": msg.to,
                    "body": msg.body,
                    "status": msg.status,
                    "direction": "Outbound" if msg.direction == "outbound-api" else "Inbound",
                    "date_sent": msg.date_sent,
                    "price": msg.price or 0  # Handle None price
                }
                for msg in messages
            ]
        except TwilioRestException as e:
            return []

    def get_call_logs(self, phone_number: str = None):
        """Get call logs using Twilio SDK."""
        try:
            params = {}
            if phone_number:
                params["from_"] = phone_number

            calls = self._client.calls.list(**params)
            return [
                {
                    "sid": call.sid,
                    "from": getattr(call, 'from_', None),  # Use from_ for outbound calls
                    "to": call.to,
                    "status": call.status,
                    "direction": "Outbound" if call.direction == "outbound-api" else "Inbound",
                    "duration": call.duration,
                    "start_time": call.start_time,
                    "price": call.price or 0  # Handle None price
                }
                for call in calls
            ]
        except TwilioRestException as e:
            return []

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
