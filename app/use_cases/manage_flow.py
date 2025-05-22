from app.models.country_data import COUNTRY_DATA

class ManageFlow:
    """
    Orchestrates all actions and logic for the Manage Numbers flow.
    Uses country_data for all country/region/price/type/capability information.
    """
    def __init__(self, twilio_gateway=None):
        self.twilio_gateway = twilio_gateway
        self.managed_numbers = []
        self.current_number = None

    def get_managed_numbers(self):
        """
        Get list of numbers under management.
        """
        if not self.twilio_gateway:
            return []

        numbers = self.twilio_gateway.list_active_numbers()
        self.managed_numbers = []
        
        for number in numbers:
            # Extract capabilities as list
            capabilities = []
            for cap, enabled in number["capabilities"].items():
                if enabled:
                    capabilities.append(cap)

            # Get country code from phone number (assuming E.164 format)
            country_code = "US"  # Default to US for now
            if number["number"].startswith("+"):
                for code in COUNTRY_DATA:
                    if number["number"].startswith("+" + COUNTRY_DATA[code].get("country_code", "")):
                        country_code = code
                        break

            # Get country code from API or phone number
            country_code = number.get("country", "US")  # Default to US if not found
            if not country_code and number["number"].startswith("+"):
                for code in COUNTRY_DATA:
                    if number["number"].startswith("+" + COUNTRY_DATA[code].get("country_code", "")):
                        country_code = code
                        break

            self.managed_numbers.append({
                "number": number["number"],
                "city": number.get("locality", "Unknown"),
                "region": number.get("region", "Unknown"),
                "country": country_code,
                "type": "local",  # Default to local if not specified
                "capabilities": capabilities,
                "monthly_cost": COUNTRY_DATA[country_code]['number_types']['local']
            })
            
        return self.managed_numbers

    def get_number_details(self, phone_number):
        """Get detailed information about a specific number"""
        # Find number in managed numbers
        for number in self.managed_numbers:
            if number['number'] == phone_number:
                self.current_number = number
                country_code = number['country']
                number_type = number['type']
                
                # Add additional details from country_data
                return {
                    **number,
                    'country_name': COUNTRY_DATA[country_code]['name'],
                    'region_code': COUNTRY_DATA[country_code]['regions'].get(number['region'], {}).get('code', ''),
                    'price': COUNTRY_DATA[country_code]['number_types'][number_type]
                }
        return None

    def get_available_configurations(self, phone_number):
        """Get available configuration options for a number"""
        number = self.get_number_details(phone_number)
        if not number:
            return {}
            
        country_code = number['country']
        number_type = number['type']
        
        # Use country_data to determine available options
        return {
            'voice_enabled': number_type in ['local', 'mobile', 'tollfree'],
            'sms_enabled': number_type in ['local', 'mobile'],
            'mms_enabled': country_code in ['US', 'CA'] and number_type in ['local', 'mobile'],
            'fax_enabled': number_type in ['local', 'tollfree']
        }

    def update_number_config(self, phone_number, config_updates):
        """
        Update configuration for a specific number.
        """
        if not self.twilio_gateway:
            return False

        number = self.get_number_details(phone_number)
        if not number:
            return False
            
        # Validate updates against available configurations
        available_config = self.get_available_configurations(phone_number)
        for key, value in config_updates.items():
            if key in available_config and value and not available_config[key]:
                return False
                
        # Update via gateway
        result = self.twilio_gateway.set_number_config(phone_number, config_updates)
        return result["success"]

    def release_number(self, phone_number):
        """
        Release a number from account.
        """
        if not self.twilio_gateway:
            return False

        number = self.get_number_details(phone_number)
        if not number:
            return False
            
        result = self.twilio_gateway.release_number(phone_number)
        if result["success"]:
            self.managed_numbers = [n for n in self.managed_numbers if n['number'] != phone_number]
            return True
        return False
