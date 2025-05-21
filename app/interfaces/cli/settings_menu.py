from app.interfaces.cli.base_menu import BaseMenu

class SettingsMenu(BaseMenu):
    def show(self):
        while True:
            options = [
                "1. Usage & Billing",
                "2. Security & Compliance",
                "3. Subaccount Management", 
                "4. Developer Tools",
                "5. Account Logs",
                "6. Advanced Search",
                "7. Configuration Management",
                "8. Logs & Diagnostics",
                "0. Back"
            ]
            self.show_panel(
                title="Settings & Admin",
                subtitle="Global and diagnostic tools",
                options=options
            )
            choice = self.prompt()
            if choice == "1":  # Usage & Billing
                self.show_panel(
                    title="Usage & Billing",
                    subtitle="View usage and cost estimates",
                    options=["Loading usage data...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "2":  # Security & Compliance
                self.show_panel(
                    title="Security & Compliance",
                    subtitle="Manage API keys, tokens, and IP whitelists",
                    options=["Loading security settings...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "3":  # Subaccount Management
                self.show_panel(
                    title="Subaccount Management",
                    subtitle="View, switch, and create subaccounts",
                    options=["Loading subaccounts...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "4":  # Developer Tools
                self.show_panel(
                    title="Developer Tools",
                    subtitle="Webhooks, Sandbox, test credentials",
                    options=["Loading developer tools...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "5":  # Account Logs
                self.show_panel(
                    title="Account Logs",
                    subtitle="View account-wide message/call/system logs",
                    options=["Loading account logs...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "6":  # Advanced Search
                self.show_panel(
                    title="Advanced Search",
                    subtitle="Deep number filtering (type, location, price)",
                    options=["Loading search options...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "7":  # Configuration Management
                self.show_panel(
                    title="Configuration Management",
                    subtitle="Bulk config tools, audit templates, cloning",
                    options=["Loading configuration tools...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "8":  # Logs & Diagnostics
                self.show_panel(
                    title="Logs & Diagnostics",
                    subtitle="View webhook errors, rate limits, failed API calls",
                    options=["Loading diagnostic data...", "0. Back"]
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "0":  # Back
                return
