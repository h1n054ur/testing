from app.models.country_data import COUNTRY_DATA

class SettingsFlow:
    """
    Manages settings, logs, developer tools, and admin operations.
    Uses country_data for all country/region/price/type/capability information.
    """
    def __init__(self):
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
        Would integrate with actual API - using sample data for now.
        """
        # Sample logs using actual country data for details
        self.current_logs = [
            {
                'timestamp': '2025-05-21 10:00:00',
                'action': 'number_purchased',
                'number': '+1234567890',
                'country': 'US',
                'type': 'local',
                'cost': COUNTRY_DATA['US']['number_types']['local'],
                'status': 'success'
            }
        ]
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
