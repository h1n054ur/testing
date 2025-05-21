from app.interfaces.cli.base_menu import BaseMenu

class ManageMenu(BaseMenu):
    def show(self):
        while True:
            # Step 2.1: View Active Numbers
            active_numbers = [
                {"index": 1, "number": "+12025550101", "location": "NY", "status": "Active", "type": "Local"},
                {"index": 2, "number": "+12025550123", "location": "CA", "status": "Active", "type": "Local"}
            ]
            
            columns = [
                {"header": "Index", "key": "index"},
                {"header": "Number", "key": "number"},
                {"header": "Location", "key": "location"},
                {"header": "Status", "key": "status"},
                {"header": "Type", "key": "type"}
            ]
            
            self.show_table(
                data=active_numbers,
                columns=columns,
                title="Active Numbers",
                subtitle="Select a number by index"
            )
            
            print("\nSelect a number by index or 0 to go back")
            choice = self.prompt()
            if choice == "0":
                return
            if choice not in ("1", "2"):
                continue

            # Step 2.2: Number-specific actions
            while True:
                options = [
                    "1. 📤 Make a Call",
                    "2. 💬 Send an SMS",
                    "3. 📄 View Logs",
                    "4. ⚙️ Configure Number",
                    "5. 🗑 Release Number",
                    "0. Back"
                ]
                self.show_panel(
                    title="Number Actions",
                    subtitle="Select an action",
                    options=options
                )
                choice = self.prompt()
                if choice == "0":  # Back to number list
                    break

                elif choice == "1":  # Make a Call
                    self.show_panel(
                        title="Make a Call",
                        subtitle="Enter destination number",
                        options=["Enter destination number:", "0. Back"]
                    )
                    choice = self.prompt()
                    if choice == "0":
                        continue
                    # Would call via SDK here

                elif choice == "2":  # Send an SMS
                    self.show_panel(
                        title="Send SMS",
                        subtitle="Enter destination and message",
                        options=["Enter destination number:", "0. Back"]
                    )
                    choice = self.prompt()
                    if choice == "0":
                        continue
                    # Would send via SDK here

                elif choice == "3":  # View Logs
                    while True:
                        options = [
                            "1. Messaging Logs",
                            "2. Call Logs",
                            "0. Back"
                        ]
                        self.show_panel(
                            title="View Logs",
                            subtitle="Select log type",
                            options=options
                        )
                        log_choice = self.prompt()
                        if log_choice == "0":
                            break
                            
                        if log_choice == "1":  # Messaging Logs
                            # Example messaging logs data
                            message_logs = [
                                {"date": "2025-05-21", "direction": "Outbound", "to": "+1234567890", "status": "Delivered", "body": "Hello there!", "price": "$0.01"},
                                {"date": "2025-05-21", "direction": "Inbound", "from": "+1234567890", "status": "Received", "body": "Hi back!", "price": "$0.00"}
                            ]
                            
                            columns = [
                                {"header": "Date", "key": "date"},
                                {"header": "Direction", "key": "direction"},
                                {"header": "To/From", "key": "to" if "to" in message_logs[0] else "from"},
                                {"header": "Status", "key": "status"},
                                {"header": "Message", "key": "body"},
                                {"header": "Price", "key": "price"}
                            ]
                            
                            current_page = 1
                            while True:
                                self.show_table(
                                    data=message_logs,
                                    columns=columns,
                                    title="Messaging Logs",
                                    subtitle="View message history",
                                    page=current_page
                                )
                                
                                print("\nPress 'n' for next page, 'p' for previous page, or '0' to go back")
                                nav_choice = self.prompt()
                                if nav_choice == "0":
                                    break
                                elif nav_choice.lower() == "n" and current_page * 10 < len(message_logs):
                                    current_page += 1
                                elif nav_choice.lower() == "p" and current_page > 1:
                                    current_page -= 1
                                    
                        elif log_choice == "2":  # Call Logs
                            # Example call logs data
                            call_logs = [
                                {"date": "2025-05-21", "direction": "Outbound", "to": "+1234567890", "duration": "2m 30s", "status": "Completed", "price": "$0.02"},
                                {"date": "2025-05-21", "direction": "Inbound", "from": "+1234567890", "duration": "1m 15s", "status": "Completed", "price": "$0.01"}
                            ]
                            
                            columns = [
                                {"header": "Date", "key": "date"},
                                {"header": "Direction", "key": "direction"},
                                {"header": "To/From", "key": "to" if "to" in call_logs[0] else "from"},
                                {"header": "Duration", "key": "duration"},
                                {"header": "Status", "key": "status"},
                                {"header": "Price", "key": "price"}
                            ]
                            
                            current_page = 1
                            while True:
                                self.show_table(
                                    data=call_logs,
                                    columns=columns,
                                    title="Call Logs",
                                    subtitle="View call history",
                                    page=current_page
                                )
                                
                                print("\nPress 'n' for next page, 'p' for previous page, or '0' to go back")
                                nav_choice = self.prompt()
                                if nav_choice == "0":
                                    break
                                elif nav_choice.lower() == "n" and current_page * 10 < len(call_logs):
                                    current_page += 1
                                elif nav_choice.lower() == "p" and current_page > 1:
                                    current_page -= 1

                elif choice == "4":  # Configure Number
                    # Show current config
                    options = [
                        "Current Configuration:",
                        "- Friendly Name: My Number",
                        "- Voice: URL (POST) https://example.com/voice",
                        "- Messaging: TwiML App (my-app)",
                        "",
                        "Actions:",
                        "1. Configure Voice",
                        "2. Configure Messaging",
                        "3. Set Friendly Name",
                        "0. Back"
                    ]
                    self.show_panel(
                        title="Configure Number",
                        subtitle="View and modify settings",
                        options=options
                    )
                    choice = self.prompt()
                    if choice == "0":
                        continue
                    # Would handle configuration here

                elif choice == "5":  # Release Number
                    options = [
                        "Are you sure you want to release this number?",
                        "+12025550101",
                        "",
                        "1. Confirm Release",
                        "0. Cancel"
                    ]
                    self.show_panel(
                        title="Release Number",
                        subtitle="Confirm release",
                        options=options
                    )
                    choice = self.prompt()
                    if choice != "1":
                        continue
                    # Would release via SDK here
