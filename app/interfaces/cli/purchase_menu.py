from app.interfaces.cli.base_menu import BaseMenu

class PurchaseMenu(BaseMenu):
    def show(self):
        # Step 1.1: Select Country
        options = [
            "1. United States (US)",
            "2. Canada (CA)",
            "3. Great Britain (GB)",
            "4. Australia (AU)",
            "5. Other (Manual Entry)",
            "0. Back"
        ]
        self.show_panel(
            title="Select Country",
            subtitle="Step 1/6 — Choose your country",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid selection. Please try again.")
            return self.show()

        # Step 1.2: Select Number Type
        options = [
            "1. Local",
            "2. Toll-Free",
            "3. Mobile",
            "0. Back"
        ]
        self.show_panel(
            title="Select Number Type",
            subtitle="Step 2/6 — Choose number type",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return self.show()
        if choice not in ["1", "2", "3"]:
            print("Invalid selection. Please try again.")
            return self.show()

        # Step 1.3: Choose Search Mode
        options = [
            "1. By Digits/Area Code",
            "2. By Locality",
            "0. Back"
        ]
        self.show_panel(
            title="Choose Search Mode",
            subtitle="Step 3/6 — Select search method",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return self.show()
        if choice not in ["1", "2"]:
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

        # Step 1.5: Begin Search
        self.show_panel(
            title="Searching Numbers",
            subtitle="Step 5/6 — Finding available numbers",
            options=["Searching... Please wait"]
        )
        # Here would be the actual API search implementation
        # with progress bar showing increments of 50

        # Step 1.6: View Results (Paginated Table)
        while True:
            options = [
                "Index  Number          City        State  Type    Price",
                "1      +1234567890    New York    NY     Local   $1.00",
                "2      +1987654321    Los Angeles CA     Local   $1.00",
                "",
                "[n] Next / [p] Previous / [s] Sort",
                "[j] Save to JSON / [c] Save to CSV",
                "Enter number index(es) to purchase (comma-separated)",
                "Example: 1,2 for multiple or just 1 for single",
                "0. Back"
            ]
            self.show_panel(
                title="Search Results",
                subtitle="Step 6/7 — View available numbers",
                options=options
            )
            choice = self.prompt()
            if choice == "0":
                return self.show()
            elif choice.lower() == "n":
                continue  # Would show next page
            elif choice.lower() == "p":
                continue  # Would show previous page
            elif choice.lower() == "s":
                continue  # Would show sort options
            elif choice.lower() == "j":
                continue  # Would save to JSON
            elif choice.lower() == "c":
                continue  # Would save to CSV
            else:
                # Try to parse as number indexes
                try:
                    indexes = [int(x.strip()) for x in choice.split(",")]
                    if all(1 <= i <= 2 for i in indexes):  # 2 is max index in our example
                        break  # Valid indexes, move to purchase step
                    print("Invalid selection. Please try again.")
                except ValueError:
                    print("Invalid selection. Please try again.")

        # Step 1.7: Select & Purchase
        options = [
            "Index  Number          City        State  Type    Price",
            "1      +1234567890    New York    NY     Local   $1.00",
            "2      +1987654321    Los Angeles CA     Local   $1.00",
            "",
            "Enter number index(es) to purchase (comma-separated)",
            "Example: 1,2 for multiple or just 1 for single",
            "",
            "0. Back"
        ]
        self.show_panel(
            title="Purchase Numbers",
            subtitle="Step 7/7 — Select numbers to purchase",
            options=options
        )
        choice = self.prompt()
        if choice == "0":
            return self.show()

        # Confirm purchase
        indexes = [x.strip() for x in choice.split(",")]
        if len(indexes) > 1:
            options = [
                f"You are about to purchase {len(indexes)} numbers:",
                *[f"  {i}. +{i}234567890" for i in indexes],
                "",
                "Total cost: ${:.2f}".format(len(indexes)),
                "",
                "1. Confirm purchase",
                "0. Cancel"
            ]
        else:
            options = [
                "You are about to purchase:",
                f"  +1234567890 (New York, NY)",
                "",
                "Cost: $1.00",
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

        # Show purchase results
        options = [
            "Purchase Results:",
            "",
            *[f"✓ +{i}234567890 - Success" for i in indexes],
            "",
            "Press any key to continue"
        ]
        self.show_panel(
            title="Purchase Complete",
            subtitle=f"{len(indexes)} number(s) purchased successfully",
            options=options
        )
        self.prompt()
