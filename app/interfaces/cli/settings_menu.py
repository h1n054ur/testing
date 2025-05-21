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
                        
                    # Example log data
                    if log_choice == "1":  # System Logs
                        system_logs = [
                            {"timestamp": "2025-05-21 10:00:00", "level": "INFO", "component": "Account", "event": "Configuration updated", "user": "admin"},
                            {"timestamp": "2025-05-21 09:45:00", "level": "WARN", "component": "Billing", "event": "Usage threshold reached", "user": "system"}
                        ]
                        
                        columns = [
                            {"header": "Timestamp", "key": "timestamp"},
                            {"header": "Level", "key": "level"},
                            {"header": "Component", "key": "component"},
                            {"header": "Event", "key": "event"},
                            {"header": "User", "key": "user"}
                        ]
                        
                    elif log_choice == "2":  # API Logs
                        system_logs = [
                            {"timestamp": "2025-05-21 10:05:00", "method": "POST", "endpoint": "/2010-04-01/Messages", "status": "200", "ip": "192.168.1.1"},
                            {"timestamp": "2025-05-21 10:00:00", "method": "GET", "endpoint": "/2010-04-01/Accounts", "status": "200", "ip": "192.168.1.1"}
                        ]
                        
                        columns = [
                            {"header": "Timestamp", "key": "timestamp"},
                            {"header": "Method", "key": "method"},
                            {"header": "Endpoint", "key": "endpoint"},
                            {"header": "Status", "key": "status"},
                            {"header": "IP", "key": "ip"}
                        ]
                        
                    elif log_choice == "3":  # Security Logs
                        system_logs = [
                            {"timestamp": "2025-05-21 10:10:00", "event": "Login attempt", "status": "Success", "ip": "192.168.1.1", "location": "New York, US"},
                            {"timestamp": "2025-05-21 10:00:00", "event": "API key created", "status": "Success", "ip": "192.168.1.1", "location": "New York, US"}
                        ]
                        
                        columns = [
                            {"header": "Timestamp", "key": "timestamp"},
                            {"header": "Event", "key": "event"},
                            {"header": "Status", "key": "status"},
                            {"header": "IP", "key": "ip"},
                            {"header": "Location", "key": "location"}
                        ]
                    
                    current_page = 1
                    while True:
                        log_type = ['System', 'API', 'Security'][int(log_choice)-1]
                        self.show_table(
                            data=system_logs,
                            columns=columns,
                            title=f"Account Logs - {log_type}",
                            subtitle=f"View {log_type.lower()} activity and events",
                            page=current_page
                        )
                        
                        print("\nPress 'n' for next page, 'p' for previous page, or '0' to go back")
                        nav_choice = self.prompt()
                        if nav_choice == "0":
                            break
                        elif nav_choice.lower() == "n" and current_page * 10 < len(system_logs):
                            current_page += 1
                        elif nav_choice.lower() == "p" and current_page > 1:
                            current_page -= 1

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
