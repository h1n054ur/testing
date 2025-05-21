from app.interfaces.cli.base_menu import BaseMenu
from app.use_cases.purchase_flow import PurchaseFlow

class PurchaseMenu(BaseMenu):
    def __init__(self, purchase_flow=None):
        super().__init__()
        self.purchase_flow = purchase_flow or PurchaseFlow()
        self.selected_country = None
        self.selected_type = None
        self.selected_region = None
        self.selected_capabilities = None

    def show(self):
        # Step 1.1: Select Country
        countries = self.purchase_flow.get_available_countries()
        options = [
            f"{i+1}. {name} ({code})" for i, (code, name) in enumerate(countries)
        ] + ["0. Back"]
        
        self.show_panel(
            title="Select Country",
            subtitle="Step 1/6 — Choose your country",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(countries):
                self.selected_country = countries[idx][0]  # Store country code
            else:
                print("Invalid selection. Please try again.")
                return self.show()
        except ValueError:
            print("Invalid selection. Please try again.")
            return self.show()

        # Step 1.2: Select Number Type
        number_types = self.purchase_flow.get_number_types(self.selected_country)
        options = [
            f"{i+1}. {type_name.title()} (${price:.2f})" for i, (type_name, price) in enumerate(number_types)
        ] + ["0. Back"]
        
        self.show_panel(
            title="Select Number Type",
            subtitle="Step 2/6 — Choose number type",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return self.show()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(number_types):
                self.selected_type = number_types[idx][0]  # Store type name
            else:
                print("Invalid selection. Please try again.")
                return self.show()
        except ValueError:
            print("Invalid selection. Please try again.")
            return self.show()

        # Step 1.3: Choose Region
        regions = self.purchase_flow.get_regions(self.selected_country)
        options = [
            f"{i+1}. {name}" for i, (name, code) in enumerate(regions)
        ] + ["0. Back"]
        
        self.show_panel(
            title="Select Region",
            subtitle="Step 3/6 — Choose region",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return self.show()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(regions):
                self.selected_region = regions[idx][0]  # Store region name
            else:
                print("Invalid selection. Please try again.")
                return self.show()
        except ValueError:
            print("Invalid selection. Please try again.")
            return self.show()

        # Step 1.4: Select Capabilities
        options = [
            "1. Voice Only",
            "2. SMS Only",
            "3. Voice & SMS",
            "0. Back"
        ]
        self.show_panel(
            title="Select Capabilities",
            subtitle="Step 4/6 — Choose number capabilities",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return self.show()
        if choice not in ["1", "2", "3"]:
            print("Invalid selection. Please try again.")
            return self.show()
            
        # Map choice to capabilities
        capabilities_map = {
            "1": ["voice"],
            "2": ["sms"],
            "3": ["voice", "sms"]
        }
        self.selected_capabilities = capabilities_map[choice]

        # Step 1.5: Begin Search
        def update_progress(current_count):
            # Calculate progress percentage (500 is target)
            progress = min(current_count / 500 * 100, 100)
            # Create progress bar (wider to fit panel)
            bar_width = 60
            filled = int(bar_width * progress / 100)
            bar = "█" * filled + "░" * (bar_width - filled)
            
            self.show_panel(
                title="Searching Numbers",
                subtitle="Step 5/6 — Finding available numbers",
                options=[
                    f"Found {current_count} unique numbers...",
                    "Searching with 1-second intervals",
                    "Will continue until 500 numbers or no new numbers found",
                    "",
                    f"Progress: {progress:.1f}%",
                    f"[{bar}]",
                    "",
                    "Please wait..."
                ]
            )

        # Initialize progress callback
        last_count = [0]
        def progress_callback(count):
            if count != last_count[0]:
                last_count[0] = count
                update_progress(count)

        # Show initial progress
        update_progress(0)
        
        # Search for numbers using the use case
        search_results = self.purchase_flow.search_numbers(
            self.selected_country,
            self.selected_type,
            self.selected_region,
            capabilities=self.selected_capabilities,
            progress_callback=progress_callback
        )
        
        if not search_results:
            self.show_panel(
                title="No Results",
                subtitle="No numbers found matching your criteria",
                options=["Press any key to try again"]
            )
            self.prompt()
            return self.show()

        # Step 1.6: View Results (Paginated Table)
        columns = [
            {"header": "Index", "key": "index"},
            {"header": "Number", "key": "number"},
            {"header": "City", "key": "city"},
            {"header": "State", "key": "state"},
            {"header": "Type", "key": "type"},
            {"header": "Price", "key": "price"}
        ]
        
        current_page = 1
        while True:
            options_text = (
                "\nOptions: [j] Save JSON, [c] Save CSV, or enter number index(es) to purchase\n"
                "Example: 1,2 for multiple or just 1 for single\n"
                "0. Back"
            )
            self.show_table(
                data=search_results,
                columns=columns,
                title="Search Results",
                subtitle="Step 6/7 — View available numbers",
                page=current_page,
                items_per_page=50,
                options_text=options_text
            )
            
            choice = self.prompt()
            if choice == "0":
                return self.show()
            elif choice.lower() == "n":
                if current_page * 50 < len(search_results):
                    current_page += 1
            elif choice.lower() == "p":
                if current_page > 1:
                    current_page -= 1
            elif choice.lower() == "j":
                continue  # Would save to JSON
            elif choice.lower() == "c":
                continue  # Would save to CSV
            else:
                # Try to parse as number indexes
                try:
                    indexes = [int(x.strip()) for x in choice.split(",")]
                    if all(1 <= i <= len(search_results) for i in indexes):
                        break  # Valid indexes, move to purchase step
                    print("Invalid selection. Please try again.")
                except ValueError:
                    print("Invalid selection. Please try again.")

        # Step 1.7: Confirm Purchase
        selected_numbers, total_cost = self.purchase_flow.get_purchase_summary(indexes)
        
        if not selected_numbers:
            print("Invalid selection. Please try again.")
            return self.show()
            
        if len(selected_numbers) > 1:
            options = [
                f"You are about to purchase {len(selected_numbers)} numbers:",
                *[f"  {n['index']}. {n['number']} ({n['city']}, {n['state']})" for n in selected_numbers],
                "",
                f"Total cost: ${total_cost:.2f}",
                "",
                "1. Confirm purchase",
                "0. Cancel"
            ]
        else:
            number = selected_numbers[0]
            options = [
                "You are about to purchase:",
                f"  {number['number']} ({number['city']}, {number['state']})",
                "",
                f"Cost: {number['price']}",
                "",
                "1. Confirm purchase",
                "0. Cancel"
            ]
        
        self.show_panel(
            title="Confirm Purchase",
            subtitle="Review your selection",
            options=options
        )
        choice = self.prompt()
        if choice != "1":
            return self.show()

        # Process purchase
        purchased_numbers = self.purchase_flow.purchase_numbers(indexes)
        
        if not purchased_numbers:
            self.show_panel(
                title="Purchase Failed",
                subtitle="Failed to purchase numbers",
                options=["Press any key to continue"]
            )
            self.prompt()
            return self.show()

        # Show purchase results
        options = [
            "Purchase Results:",
            "",
            *[f"✓ {n['number']} - Success" for n in purchased_numbers],
            "",
            "Press any key to continue"
        ]
        self.show_panel(
            title="Purchase Complete",
            subtitle=f"{len(purchased_numbers)} number(s) purchased successfully",
            options=options
        )
        self.prompt()