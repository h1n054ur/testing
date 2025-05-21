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
        """
        Get current account settings.
        Would integrate with actual API - using sample data for now.
        """
        # Sample settings using actual country data for defaults
        self.current_settings = {
            'default_country': 'US',
            'default_number_type': 'local',
            'default_capabilities': ['voice', 'sms'],
            'pricing_tier': 'standard',
            'monthly_spend_limit': 1000.00,
            'notification_email': 'admin@example.com',
            'auto_renew': True
        }
        return self.current_settings

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
        """
        Get billing summary including costs from country_data.
        Would integrate with actual API - using sample data for now.
        """
        settings = self.get_account_settings()
        country = settings['default_country']
        number_type = settings['default_number_type']
        
        # Use actual pricing from country_data
        if country in COUNTRY_DATA and number_type in COUNTRY_DATA[country]['number_types']:
            price_per_number = COUNTRY_DATA[country]['number_types'][number_type]
        else:
            price_per_number = 0
            
        return {
            'active_numbers': 5,
            'price_per_number': price_per_number,
            'monthly_recurring': price_per_number * 5,
            'spend_limit': settings['monthly_spend_limit'],
            'current_usage': price_per_number * 5 * 0.8,  # 80% of monthly cost as sample usage
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
        logs = self.twilio_gateway.get_account_logs()
        if not isinstance(logs, dict):
            return []

        # Format logs
        self.current_logs = []
        
        # Process message logs
        for msg in logs.get("messages", []):
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
        for call in logs.get("calls", []):
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
        """
        Update account settings.
        Would integrate with actual API - using mock for now.
        """
        # Validate country and number type against country_data
        if 'default_country' in new_settings:
            if new_settings['default_country'] not in COUNTRY_DATA:
                return False
                
        if 'default_number_type' in new_settings and 'default_country' in new_settings:
            country = new_settings['default_country']
            number_type = new_settings['default_number_type']
            if number_type not in COUNTRY_DATA[country]['number_types']:
                return False
                
        # Mock successful update
        self.current_settings.update(new_settings)
        return True

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
