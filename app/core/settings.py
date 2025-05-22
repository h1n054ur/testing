from app.models.country_data import COUNTRY_DATA

class SettingsFlow:
    """
    Manages settings, logs, developer tools, and admin operations.
    Uses country_data for all country/region/price/type/capability information.
    """
    def __init__(self, twilio_gateway=None):
        self.twilio_gateway = twilio_gateway
        self.current_settings = {}
        self.current_logs = []

    def get_account_settings(self):
        """Get current account settings from Twilio."""
        if not self.twilio_gateway:
            return self._get_default_settings()

        # Get account details
        account_result = self.twilio_gateway.get_account_details()
        if not account_result.get("success"):
            return self._get_default_settings()

        account = account_result["account"]
        
        # Get account balance
        balance_result = self.twilio_gateway.get_account_balance()
        balance = balance_result.get("balance", {}) if balance_result.get("success") else {}

        # Get active numbers
        numbers_result = self.twilio_gateway.list_active_numbers()
        numbers = numbers_result.get("numbers", []) if numbers_result.get("success") else []

        # Build settings
        self.current_settings = {
            'account_sid': account['sid'],
            'friendly_name': account['friendly_name'],
            'account_type': account['type'],
            'account_status': account['status'],
            'balance': balance.get('balance', 0.0),
            'currency': balance.get('currency', 'USD'),
            'active_numbers': len(numbers),
            'default_country': 'US',  # Keep defaults for UI
            'default_number_type': 'local',
            'default_capabilities': ['voice', 'sms']
        }
        return self.current_settings

    def _get_default_settings(self):
        """Return default settings when Twilio is not available."""
        return {
            'default_country': 'US',
            'default_number_type': 'local',
            'default_capabilities': ['voice', 'sms'],
            'pricing_tier': 'standard',
            'monthly_spend_limit': 1000.00,
            'notification_email': 'admin@example.com',
            'auto_renew': True
        }

    def get_country_pricing(self, country_code):
        """Get detailed pricing information for a country"""
        if country_code not in COUNTRY_DATA:
            return None
            
        return {
            'country_name': COUNTRY_DATA[country_code]['name'],
            'number_types': COUNTRY_DATA[country_code]['number_types'],
            'regions_count': len(COUNTRY_DATA[country_code]['regions'])
        }

    def get_billing_summary(self):
        """Get billing summary from Twilio."""
        if not self.twilio_gateway:
            return self._get_default_billing()

        # Get account balance
        balance_result = self.twilio_gateway.get_account_balance()
        if not balance_result.get("success"):
            return self._get_default_billing()

        balance = balance_result["balance"]

        # Get active numbers
        numbers_result = self.twilio_gateway.list_active_numbers()
        numbers = numbers_result.get("numbers", []) if numbers_result.get("success") else []

        # Calculate costs based on actual numbers
        total_cost = 0
        for number in numbers:
            country_code = number["number"][:2]  # Extract country code from number
            number_type = "local"  # Default to local
            if number["capabilities"].get("voice") and number["capabilities"].get("sms"):
                number_type = "local"
            elif number["capabilities"].get("sms"):
                number_type = "mobile"
            elif number["capabilities"].get("voice"):
                number_type = "tollfree"

            # Get price from country_data
            if country_code in COUNTRY_DATA and number_type in COUNTRY_DATA[country_code]['number_types']:
                total_cost += COUNTRY_DATA[country_code]['number_types'][number_type]

        return {
            'active_numbers': len(numbers),
            'price_per_number': total_cost / len(numbers) if numbers else 0,
            'monthly_recurring': total_cost,
            'spend_limit': 1000.00,  # Default limit
            'current_usage': float(balance["balance"]),
            'billing_cycle': 'Monthly',
            'next_bill_date': '2025-06-01'  # TODO: Calculate from billing cycle
        }

    def _get_default_billing(self):
        """Return default billing when Twilio is not available."""
        return {
            'active_numbers': 0,
            'price_per_number': 0,
            'monthly_recurring': 0,
            'spend_limit': 1000.00,
            'current_usage': 0,
            'billing_cycle': 'Monthly',
            'next_bill_date': '2025-06-01'
        }

    def get_activity_logs(self, filters=None):
        """
        Get activity logs with country-specific details.
        """
        if not self.twilio_gateway:
            return []

        # Get logs from gateway
        result = self.twilio_gateway.get_account_logs()
        if not result.get("success", False):
            print(f"Error getting account logs: {result.get('error', 'Unknown error')}")
            return []

        # Format logs
        self.current_logs = []
        
        # Get logs from gateway
        result = self.twilio_gateway.get_account_logs()
        if not result.get("success", False):
            print(f"Error getting account logs: {result.get('error', 'Unknown error')}")
            return []

        # Process message logs
        message_logs = result.get("messages", {}).get("messages", [])
        for msg in message_logs:
            self.current_logs.append({
                'timestamp': str(msg.get('date_sent', '')),
                'action': 'message_sent' if msg.get('direction') == 'outbound' else 'message_received',
                'number': msg.get('from'),
                'to': msg.get('to'),
                'type': 'sms',
                'cost': msg.get('price', '0.00'),
                'status': msg.get('status', 'unknown')
            })

        # Process call logs
        call_logs = result.get("calls", {}).get("calls", [])
        for call in call_logs:
            self.current_logs.append({
                'timestamp': str(call.get('start_time', '')),
                'action': 'call_made' if call.get('direction') == 'outbound' else 'call_received',
                'number': call.get('from'),
                'to': call.get('to'),
                'type': 'voice',
                'cost': call.get('price', '0.00'),
                'status': call.get('status', 'unknown'),
                'duration': call.get('duration', '0')
            })

        # Sort by timestamp
        self.current_logs.sort(key=lambda x: x['timestamp'], reverse=True)
        
        return self.current_logs

    def update_settings(self, new_settings):
        """Update account settings using Twilio SDK."""
        if not self.twilio_gateway:
            return False

        # Validate country and number type against country_data
        if 'default_country' in new_settings:
            if new_settings['default_country'] not in COUNTRY_DATA:
                return False
                
        if 'default_number_type' in new_settings and 'default_country' in new_settings:
            country = new_settings['default_country']
            number_type = new_settings['default_number_type']
            if number_type not in COUNTRY_DATA[country]['number_types']:
                return False

        # Update friendly name if provided
        if 'friendly_name' in new_settings:
            result = self.twilio_gateway._client.api.accounts(self.twilio_gateway._account_sid).update(
                friendly_name=new_settings['friendly_name']
            )
            if not result:
                return False

        # Store UI preferences locally
        self.current_settings.update({
            k: v for k, v in new_settings.items() 
            if k in ['default_country', 'default_number_type', 'default_capabilities']
        })
        return True

    def get_subaccounts(self):
        """Get list of subaccounts."""
        if not self.twilio_gateway:
            return []

        result = self.twilio_gateway.get_subaccounts()
        if not result.get("success"):
            return []

        return result["accounts"]

    def create_subaccount(self, friendly_name):
        """Create a new subaccount."""
        if not self.twilio_gateway:
            return {"success": False, "error": "Twilio gateway not available"}

        result = self.twilio_gateway.create_subaccount(friendly_name)
        if not result.get("success"):
            return {"success": False, "error": result.get("error", "Unknown error")}

        return {
            "success": True,
            "sid": result["sid"],
            "auth_token": result["auth_token"]
        }

    def close_subaccount(self, account_sid):
        """Close/suspend a subaccount."""
        if not self.twilio_gateway:
            return {"success": False, "error": "Twilio gateway not available"}

        result = self.twilio_gateway.close_subaccount(account_sid)
        if not result.get("success"):
            return {"success": False, "error": result.get("error", "Unknown error")}

        return {"success": True}

    def switch_account(self, account_sid):
        """Switch to a different subaccount."""
        if not self.twilio_gateway:
            return {"success": False, "error": "Twilio gateway not available"}

        # Get the subaccount's auth token
        accounts = self.get_subaccounts()
        auth_token = None
        for account in accounts:
            if account["sid"] == account_sid:
                auth_token = account["auth_token"]
                break

        if not auth_token:
            return {"success": False, "error": "Account not found"}

        try:
            # Create new gateway instance with subaccount credentials
            self.twilio_gateway = TwilioGateway(account_sid, auth_token)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_api_credentials(self):
        """Get API credentials."""
        if not self.twilio_gateway:
            return {
                "account_sid": None,
                "auth_token": None
            }

        return {
            "account_sid": self.twilio_gateway._account_sid,
            "auth_token": self.twilio_gateway._auth_token
        }

    def get_webhook_settings(self):
        """Get webhook settings."""
        if not self.twilio_gateway:
            return {
                "voice_url": None,
                "sms_url": None,
                "status_url": None
            }

        result = self.twilio_gateway.get_webhook_settings()
        if not result.get("success"):
            return {
                "voice_url": None,
                "sms_url": None,
                "status_url": None
            }

        webhooks = result["webhooks"]
        return {
            "voice_url": webhooks["voice"][0]["url"] if webhooks["voice"] else None,
            "sms_url": webhooks["sms"][0]["url"] if webhooks["sms"] else None,
            "status_url": webhooks["status"][0]["url"] if webhooks["status"] else None
        }

    def set_webhook_settings(self, webhook_type, url, method="POST"):
        """Set webhook URL."""
        if not self.twilio_gateway:
            return {"success": False, "error": "Twilio gateway not available"}

        result = self.twilio_gateway.set_webhook_settings(webhook_type, url, method)
        if not result.get("success"):
            return {"success": False, "error": result.get("error", "Unknown error")}

        return {"success": True}

    def export_logs(self, format='json'):
        """
        Export logs in specified format.
        Returns string representation of logs.
        """
        logs = self.get_activity_logs()
        if format == 'json':
            import json
            return json.dumps(logs, indent=2)
        elif format == 'csv':
            import csv
            import io
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=logs[0].keys())
            writer.writeheader()
            writer.writerows(logs)
            return output.getvalue()
        return None
