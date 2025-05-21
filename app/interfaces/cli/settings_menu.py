from app.interfaces.cli.base_menu import BaseMenu
from app.use_cases.settings_flow import SettingsFlow

class SettingsMenu(BaseMenu):
    def __init__(self, settings_flow=None):
        super().__init__()
        self.settings_flow = settings_flow or SettingsFlow()

    def show(self):
        while True:
            # Get current settings from use case
            settings = self.settings_flow.get_account_settings()
            
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
                # Get billing summary from use case
                billing = self.settings_flow.get_billing_summary()
                options = [
                    "Current Usage:",
                    f"Active Numbers: {billing['active_numbers']}",
                    f"Price per Number: ${billing['price_per_number']:.2f}",
                    f"Monthly Recurring: ${billing['monthly_recurring']:.2f}",
                    "",
                    "Billing Settings:",
                    f"Spend Limit: ${billing['spend_limit']:.2f}",
                    f"Current Usage: ${billing['current_usage']:.2f}",
                    f"Billing Cycle: {billing['billing_cycle']}",
                    f"Next Bill Date: {billing['next_bill_date']}",
                    "",
                    "0. Back"
                ]
                self.show_panel(
                    title="Usage & Billing",
                    subtitle="View usage and cost estimates",
                    options=options
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "2":  # Security & Compliance
                options = [
                    "Current Settings:",
                    f"Default Country: {settings['default_country']}",
                    f"Default Number Type: {settings['default_number_type']}",
                    f"Default Capabilities: {', '.join(settings['default_capabilities'])}",
                    "",
                    "Actions:",
                    "1. Update Default Country",
                    "2. Update Default Number Type",
                    "3. Update Default Capabilities",
                    "0. Back"
                ]
                self.show_panel(
                    title="Security & Compliance",
                    subtitle="Manage API keys, tokens, and IP whitelists",
                    options=options
                )
                choice = self.prompt()
                if choice == "0":
                    continue
                    
                # Handle settings updates
                if choice in ["1", "2", "3"]:
                    # Example: Update default country
                    if choice == "1":
                        self.settings_flow.update_settings({'default_country': 'US'})

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
                while True:
                    options = [
                        "1. System Logs",
                        "2. API Logs",
                        "3. Security Logs",
                        "0. Back"
                    ]
                    self.show_panel(
                        title="Account Logs",
                        subtitle="Select log type to view",
                        options=options
                    )
                    log_choice = self.prompt()
                    if log_choice == "0":
                        break
                        
                    # Get logs from use case
                    logs = self.settings_flow.get_activity_logs()
                    
                    columns = [
                        {"header": "Timestamp", "key": "timestamp"},
                        {"header": "Action", "key": "action"},
                        {"header": "Number", "key": "number"},
                        {"header": "Country", "key": "country"},
                        {"header": "Type", "key": "type"},
                        {"header": "Cost", "key": "cost"},
                        {"header": "Status", "key": "status"}
                    ]
                    
                    current_page = 1
                    while True:
                        self.show_table(
                            data=logs,
                            columns=columns,
                            title="Account Logs",
                            subtitle="View account activity",
                            page=current_page,
                            options_text="\nOptions: [j] Save JSON, [c] Save CSV, or '0' to go back"
                        )
                        nav_choice = self.prompt()
                        if nav_choice == "0":
                            break
                        elif nav_choice.lower() == "n" and current_page * 10 < len(logs):
                            current_page += 1
                        elif nav_choice.lower() == "p" and current_page > 1:
                            current_page -= 1
                        elif nav_choice.lower() == "j":
                            # Export logs as JSON
                            log_data = self.settings_flow.export_logs(format='json')
                            print("\nExported logs to JSON format")
                            print(log_data)
                        elif nav_choice.lower() == "c":
                            # Export logs as CSV
                            log_data = self.settings_flow.export_logs(format='csv')
                            print("\nExported logs to CSV format")
                            print(log_data)

            elif choice == "6":  # Advanced Search
                # Get country pricing info for search options
                countries = [
                    ('US', self.settings_flow.get_country_pricing('US')),
                    ('CA', self.settings_flow.get_country_pricing('CA')),
                    ('GB', self.settings_flow.get_country_pricing('GB')),
                    ('AU', self.settings_flow.get_country_pricing('AU'))
                ]
                
                options = ["Available Search Options:"]
                for code, pricing in countries:
                    if pricing:
                        options.append(f"\n{pricing['country_name']}:")
                        for type_name, price in pricing['number_types'].items():
                            options.append(f"- {type_name.title()}: ${price:.2f}")
                        options.append(f"- {pricing['regions_count']} regions available")
                options.extend(["", "0. Back"])
                
                self.show_panel(
                    title="Advanced Search",
                    subtitle="Deep number filtering (type, location, price)",
                    options=options
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "7":  # Configuration Management
                # Get current settings for display
                settings = self.settings_flow.get_account_settings()
                options = [
                    "Current Configuration:",
                    f"Default Country: {settings['default_country']}",
                    f"Default Number Type: {settings['default_number_type']}",
                    f"Default Capabilities: {', '.join(settings['default_capabilities'])}",
                    f"Pricing Tier: {settings['pricing_tier']}",
                    f"Monthly Spend Limit: ${settings['monthly_spend_limit']:.2f}",
                    f"Notification Email: {settings['notification_email']}",
                    f"Auto Renew: {'Yes' if settings['auto_renew'] else 'No'}",
                    "",
                    "Actions:",
                    "1. Update Settings",
                    "2. Export Configuration",
                    "3. Import Configuration",
                    "0. Back"
                ]
                self.show_panel(
                    title="Configuration Management",
                    subtitle="Manage global settings",
                    options=options
                )
                choice = self.prompt()
                if choice == "0":
                    continue

            elif choice == "8":  # Logs & Diagnostics
                # Get activity logs for diagnostics
                logs = self.settings_flow.get_activity_logs()
                
                options = [
                    "Diagnostic Summary:",
                    f"Total Log Entries: {len(logs)}",
                    "",
                    "Actions:",
                    "1. View Detailed Logs",
                    "2. Export Logs (JSON)",
                    "3. Export Logs (CSV)",
                    "0. Back"
                ]
                self.show_panel(
                    title="Logs & Diagnostics",
                    subtitle="View system logs and diagnostics",
                    options=options
                )
                choice = self.prompt()
                if choice == "0":
                    continue
                elif choice == "2":
                    log_data = self.settings_flow.export_logs(format='json')
                    print("\nExported logs to JSON format")
                    print(log_data)
                elif choice == "3":
                    log_data = self.settings_flow.export_logs(format='csv')
                    print("\nExported logs to CSV format")
                    print(log_data)

            elif choice == "0":  # Back
                return