from app.models.country_data import COUNTRY_DATA

class PurchaseFlow:
    """
    Handles all steps for searching and purchasing phone numbers.
    Uses country_data for all country/region/price/type/capability information.
    """
    def __init__(self):
        self.selected_country = None
        self.selected_type = None
        self.selected_region = None
        self.selected_capabilities = None
        self.search_results = []

    def get_available_countries(self):
        """Returns list of available countries with their codes"""
        return [(code, data['name']) for code, data in COUNTRY_DATA.items()]

    def get_number_types(self, country_code):
        """Returns available number types and prices for a country"""
        if country_code not in COUNTRY_DATA:
            return []
        return [(type_name, price) for type_name, price in COUNTRY_DATA[country_code]['number_types'].items()]

    def get_regions(self, country_code):
        """Returns available regions for a country"""
        if country_code not in COUNTRY_DATA:
            return []
        return [(name, data['code']) for name, data in COUNTRY_DATA[country_code]['regions'].items()]

    def get_area_codes(self, country_code, region_name):
        """Returns area codes for a region in a country"""
        if country_code not in COUNTRY_DATA or region_name not in COUNTRY_DATA[country_code]['regions']:
            return []
        return COUNTRY_DATA[country_code]['regions'][region_name]['area_codes']

    def search_numbers(self, country_code, number_type, region=None, area_code=None, capabilities=None):
        """
        Search for available numbers based on criteria.
        Returns list of number details including pricing from country_data.
        """
        # This would integrate with actual number search API
        # For now returning sample data with correct pricing from country_data
        if country_code not in COUNTRY_DATA:
            return []
            
        price = COUNTRY_DATA[country_code]['number_types'].get(number_type, 0)
        
        # Sample results using actual pricing from country_data
        self.search_results = [
            {
                "index": 1,
                "number": "+1234567890",
                "city": region or "Any",
                "state": COUNTRY_DATA[country_code]['regions'].get(region, {}).get('code', ''),
                "type": number_type,
                "price": f"${price:.2f}"
            }
        ]
        return self.search_results

    def get_purchase_summary(self, selected_indexes):
        """
        Get summary of numbers to be purchased including total cost
        """
        if not self.search_results:
            return None, 0
            
        selected_numbers = []
        total_cost = 0
        
        for idx in selected_indexes:
            if 1 <= idx <= len(self.search_results):
                number = self.search_results[idx-1]
                selected_numbers.append(number)
                price = float(number['price'].replace('$', ''))
                total_cost += price
                
        return selected_numbers, total_cost

    def purchase_numbers(self, selected_indexes):
        """
        Purchase selected numbers. Returns list of successful purchases.
        """
        numbers, _ = self.get_purchase_summary(selected_indexes)
        if not numbers:
            return []
            
        # This would integrate with actual purchase API
        # For now just return the numbers as if purchase was successful
        return numbers
