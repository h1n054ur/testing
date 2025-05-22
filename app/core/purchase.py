from app.models.country_data import COUNTRY_DATA

class PurchaseFlow:
    """
    Handles all steps for searching and purchasing phone numbers.
    Uses country_data for all country/region/price/type/capability information.
    """
    def __init__(self, twilio_gateway=None):
        self.twilio_gateway = twilio_gateway
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
        # Only return types that have a price (not None)
        return [(type_name, price) for type_name, price in COUNTRY_DATA[country_code]['number_types'].items() if price is not None]

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

    def get_all_area_codes(self, country_code):
        """Returns all area codes for a country"""
        if country_code not in COUNTRY_DATA:
            return []
        area_codes = set()
        for region_data in COUNTRY_DATA[country_code]['regions'].values():
            area_codes.update(region_data['area_codes'])
        return sorted(list(area_codes))

    def search_numbers(self, country_code, number_type, region=None, pattern=None, progress_callback=None):
        """
        Search for available numbers based on criteria.
        Continues searching until either:
        - 500 unique numbers are found
        - 3 consecutive requests return no new numbers
        - User presses Enter to stop search
        Returns list of number details including pricing from country_data.

        Args:
            country_code: Country code (e.g., 'US')
            number_type: Type of number ('local', 'mobile', 'tollfree')
            region: Optional region name
            pattern: Optional pattern to search for (2-10 digits)
            progress_callback: Optional callback function(count) to report progress
        """
        if not self.twilio_gateway:
            return []

        if country_code not in COUNTRY_DATA:
            return []
            
        # Handle pattern search for US 3-digit area code match
        area_code = None
        if pattern and country_code == 'US' and len(pattern) == 3:
            # Check if pattern matches any US area code
            all_area_codes = self.get_all_area_codes('US')
            if int(pattern) in all_area_codes:
                area_code = pattern
                pattern = None  # Clear pattern since we'll search by area code

        # Track unique numbers, failed attempts, and all results
        seen_numbers = set()
        all_results = {}  # number -> full result mapping
        no_new_numbers_count = 0
        page = 1
        limit = 30  # Numbers per page
        stop_search = False

        def check_for_enter():
            import sys
            import select
            # Check if there's input available
            if select.select([sys.stdin], [], [], 0)[0]:
                # Clear the input buffer
                sys.stdin.readline()
                return True
            return False

        while len(seen_numbers) < 500 and no_new_numbers_count < 3 and not stop_search:
            # Check for Enter key
            if check_for_enter():
                break

            # Search using gateway
            results = self.twilio_gateway.search_available_numbers(
                country_code=country_code,
                number_type=number_type,
                region=region,
                area_code=area_code,
                pattern=pattern,
                page=page,
                limit=limit
            )

            # Track new unique numbers
            new_numbers_found = False
            if not results.get("success", False):
                print(f"Error searching numbers: {results.get('error', 'Unknown error')}")
                break

            for result in results.get("numbers", []):
                number = result["number"]
                if number not in seen_numbers:
                    seen_numbers.add(number)
                    all_results[number] = result
                    new_numbers_found = True
                    # Report progress if callback provided
                    if progress_callback:
                        progress_callback(len(seen_numbers))

            # Update counters
            if not new_numbers_found:
                no_new_numbers_count += 1
            else:
                no_new_numbers_count = 0

            # Sleep for 1 second before next request
            import time
            time.sleep(1)
            page += 1

        # Format final results with index
        self.search_results = []
        for i, number in enumerate(seen_numbers, 1):
            result = all_results[number]
            # Get price from country_data
            price = COUNTRY_DATA[country_code]['number_types'].get(number_type, 0)
            self.search_results.append({
                "index": i,
                "number": number,
                "city": result["city"],
                "state": result["state"],
                "type": result["type"],
                "price": f"${price:.2f}",
                "capabilities": result.get("capabilities", {})
            })
        
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
        if not self.twilio_gateway:
            return []

        numbers, _ = self.get_purchase_summary(selected_indexes)
        if not numbers:
            return []
            
        successful_purchases = []
        for number in numbers:
            result = self.twilio_gateway.purchase_number(number["number"])
            if result["success"]:
                successful_purchases.append(number)
                
        return successful_purchases

    def save_search_results(self, format='json'):
        """Save search results to file in specified format"""
        if not self.search_results:
            return {"success": False, "error": "No search results to save"}

        try:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if format == 'json':
                import json
                filename = f"search_results_{timestamp}.json"
                with open(filename, "w") as f:
                    json.dump(self.search_results, f, indent=2)
            elif format == 'csv':
                import csv
                filename = f"search_results_{timestamp}.csv"
                with open(filename, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=["index", "number", "city", "state", "type", "price"])
                    writer.writeheader()
                    writer.writerows(self.search_results)
            else:
                return {"success": False, "error": "Invalid format specified"}
                
            return {"success": True, "filename": filename}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def sort_search_results(self, sort_key):
        """Sort search results by specified key"""
        if not self.search_results:
            return {"success": False, "error": "No search results to sort"}
            
        valid_keys = ["number", "city", "state", "type", "price"]
        if sort_key not in valid_keys:
            return {"success": False, "error": "Invalid sort key"}
            
        try:
            # Handle price specially since it's a string with currency symbol
            if sort_key == "price":
                self.search_results.sort(key=lambda x: float(x[sort_key].replace("$", "")))
            else:
                self.search_results.sort(key=lambda x: x[sort_key])
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}
