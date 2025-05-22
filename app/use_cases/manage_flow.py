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

    def _detect_number_info(self, phone_number):
        """
        Helper method to detect number type, region and price based on number format.
        Returns dict with detected info.
        """
        # Initialize with default values
        info = {
            "country": "Unknown",
            "type": "N/A",
            "region": "N/A",
            "monthly_cost": "N/A"
        }
        
        if not phone_number.startswith("+"):
            return info

        # Step 1: Detect country
        number = phone_number[1:]  # Remove + prefix
        if number.startswith("1"):  # US/CA
            # Check area code to distinguish between US and CA
            area_code = int(number[1:4])
            # Check US first since it has more area codes
            for region, data in COUNTRY_DATA["US"]["regions"].items():
                if area_code in data["area_codes"]:
                    info["country"] = "US"
                    break
            if info["country"] == "Unknown":  # Not found in US, check CA
                for region, data in COUNTRY_DATA["CA"]["regions"].items():
                    if area_code in data["area_codes"]:
                        info["country"] = "CA"
                        break
        elif number.startswith("44"):  # GB
            info["country"] = "GB"
        elif number.startswith("61"):  # AU
            info["country"] = "AU"

        if info["country"] == "Unknown":
            return info

        country_data = COUNTRY_DATA[info["country"]]
        
        # Step 2: Detect number type and region
        if info["country"] in ["US", "CA"]:
            area_code = int(number[1:4])
            # Check for tollfree first
            if area_code in country_data["tollfree_prefixes"]:
                info["type"] = "tollfree"
                info["region"] = "N/A"
            else:
                # Check for local number region
                for region, data in country_data["regions"].items():
                    if area_code in data["area_codes"]:
                        info["type"] = "local"
                        info["region"] = region
                        break

        elif info["country"] == "GB":
            area_code = number[2:]  # Remove country code
            # Check for mobile
            if area_code.startswith("7"):
                info["type"] = "mobile"
                info["region"] = "N/A"
            # Check for tollfree
            elif any(area_code.startswith(str(prefix)) for prefix in country_data["tollfree_prefixes"]):
                info["type"] = "tollfree"
                info["region"] = "N/A"
            else:
                # Check for local number region
                for region, data in country_data["regions"].items():
                    for code in data["area_codes"]:
                        if isinstance(code, tuple):
                            # Handle range tuple
                            start, end = code
                            if area_code.startswith(str(start)[:len(str(start))]):
                                area_num = int(area_code[:len(str(start))])
                                if start <= area_num <= end:
                                    info["type"] = "local"
                                    info["region"] = region
                                    break
                        else:
                            # Handle single integer code
                            if area_code.startswith(str(code)):
                                info["type"] = "local"
                                info["region"] = region
                                break
                    if info["type"] == "local":
                        break

        elif info["country"] == "AU":
            # Check for mobile (starts with 4 after country code)
            if number[2] == "4":
                info["type"] = "mobile"
                info["region"] = "N/A"
            # Check for tollfree
            elif any(number[2:].startswith(str(prefix)) for prefix in country_data["tollfree_prefixes"]):
                info["type"] = "tollfree"
                info["region"] = "N/A"
            else:
                # Check for local number region
                area_code = int(number[2:5])
                for region, data in country_data["regions"].items():
                    if area_code in data["area_codes"]:
                        info["type"] = "local"
                        info["region"] = region
                        break

        # Step 3: Set price based on type
        if info["type"] != "N/A":
            price = country_data["number_types"][info["type"]]
            info["monthly_cost"] = f"${price:.2f}"
        else:
            info["monthly_cost"] = "N/A"

        return info

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

            # Detect number information
            info = self._detect_number_info(number["number"])
            
            self.managed_numbers.append({
                "number": number["number"],
                "country": info["country"],
                "region": info["region"],
                "type": info["type"],
                "capabilities": capabilities,
                "monthly_cost": info["monthly_cost"]
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

    def send_sms(self, from_number, to_number, message):
        """
        Send SMS using the gateway.
        Returns dict with success status and details.
        """
        if not self.twilio_gateway:
            return {
                "success": False,
                "error": "Gateway not initialized"
            }

        # Verify the from number is managed
        number = self.get_number_details(from_number)
        if not number:
            return {
                "success": False,
                "error": "From number not found in managed numbers"
            }

        # Send via gateway
        return self.twilio_gateway.send_sms(from_number, to_number, message)

    def make_call(self, from_number, to_number, twiml=None):
        """
        Make a call using the gateway.
        Returns dict with success status and details.
        """
        if not self.twilio_gateway:
            return {
                "success": False,
                "error": "Gateway not initialized"
            }

        # Verify the from number is managed
        number = self.get_number_details(from_number)
        if not number:
            return {
                "success": False,
                "error": "From number not found in managed numbers"
            }

        # Make call via gateway
        return self.twilio_gateway.make_call(from_number, to_number, twiml=twiml)

    def get_message_logs(self, phone_number):
        """
        Get message logs for a specific number.
        Returns list of message records with details.
        """
        if not self.twilio_gateway:
            return []

        # Verify the number is managed
        number = self.get_number_details(phone_number)
        if not number:
            return []

        # Get logs from gateway
        logs = self.twilio_gateway.get_messaging_logs(phone_number)
        
        # Format logs for display
        return [
            {
                "date": str(log["date_sent"].date()) if log["date_sent"] else "N/A",
                "direction": log["direction"],  # Already formatted in gateway
                "to" if log["direction"] == "Outbound" else "from": log["to" if log["direction"] == "Outbound" else "from"] or "Unknown",
                "status": log["status"].title(),
                "body": log["body"] or "",
                "price": f"${float(log['price']):.2f}"  # Price is already defaulted to 0 in gateway
            }
            for log in logs
        ]

    def get_call_logs(self, phone_number):
        """
        Get call logs for a specific number.
        Returns list of call records with details.
        """
        if not self.twilio_gateway:
            return []

        # Verify the number is managed
        number = self.get_number_details(phone_number)
        if not number:
            return []

        # Get logs from gateway
        logs = self.twilio_gateway.get_call_logs(phone_number)
        
        # Format logs for display
        return [
            {
                "date": str(log["start_time"].date()) if log["start_time"] else "N/A",
                "direction": log["direction"],  # Already formatted in gateway
                "to" if log["direction"] == "Outbound" else "from": log["to" if log["direction"] == "Outbound" else "from"] or "Unknown",
                "duration": f"{int(log['duration'] or 0)}s",
                "status": log["status"].title(),
                "price": f"${float(log['price']):.2f}"  # Price is already defaulted to 0 in gateway
            }
            for log in logs
        ]
