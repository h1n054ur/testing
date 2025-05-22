from app.interfaces.cli.base_menu import BaseMenu
from app.use_cases.manage_flow import ManageFlow

class ManageMenu(BaseMenu):
    def __init__(self, manage_flow=None):
        super().__init__()
        self.manage_flow = manage_flow or ManageFlow()
        self.current_number = None

    def show(self):
        while True:
            # Step 2.1: View Active Numbers
            active_numbers = self.manage_flow.get_managed_numbers()
            if not active_numbers:
                self.show_panel(
                    title="No Active Numbers",
                    subtitle="You don't have any numbers yet",
                    options=["Press any key to go back"]
                )
                self.prompt()
                return
                
            # Add index to each number for display
            for i, number in enumerate(active_numbers, 1):
                number['index'] = i
            
            columns = [
                {"header": "Index", "key": "index"},
                {"header": "Number", "key": "number"},
                {"header": "Region", "key": "region"},
                {"header": "Country", "key": "country"},
                {"header": "Type", "key": "type"},
                {"header": "Monthly Cost", "key": "monthly_cost"}
            ]
            
            self.show_table(
                data=active_numbers,
                columns=columns,
                title="Active Numbers",
                subtitle="Select a number by index",
                options_text="\nSelect a number by index or 0 to go back"
            )
            choice = self.prompt()
            if choice == "0":
                return
            try:
                idx = int(choice)
                if not (1 <= idx <= len(active_numbers)):
                    print("Invalid selection. Please try again.")
                    continue
                self.current_number = active_numbers[idx-1]['number']
            except ValueError:
                print("Invalid selection. Please try again.")
                continue

            # Step 2.2: Number-specific actions
            while True:
                # Get number details from use case
                number_details = self.manage_flow.get_number_details(self.current_number)
                if not number_details:
                    print("Error: Number details not found")
                    break
                    
                # Get available configurations
                config = self.manage_flow.get_available_configurations(self.current_number)
                
                options = [
                    f"Selected: {number_details['number']} ({number_details['region']}, {number_details['country_name']})",
                    f"Type: {number_details['type'].title()}, Monthly Cost: ${number_details['price']:.2f}",
                    "",
                    "1. 📤 Make a Call" if config.get('voice_enabled') else "1. ❌ Voice not available",
                    "2. 💬 Send an SMS" if config.get('sms_enabled') else "2. ❌ SMS not available",
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

                elif choice == "1" and config.get('voice_enabled'):  # Make a Call
                    self.show_panel(
                        title="Make a Call",
                        subtitle="Enter destination number",
                        options=["Enter destination number:", "0. Back"]
                    )
                    choice = self.prompt()
                    if choice == "0":
                        continue
                    # Would call via SDK here

                elif choice == "2" and config.get('sms_enabled'):  # Send an SMS
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
                            "1. Messaging Logs" if config.get('sms_enabled') else "1. ❌ Messaging not available",
                            "2. Call Logs" if config.get('voice_enabled') else "2. ❌ Voice not available",
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
                            
                        if log_choice == "1" and config.get('sms_enabled'):  # Messaging Logs
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
                                    page=current_page,
                                    options_text="\nPress '0' to go back"
                                )
                                nav_choice = self.prompt()
                                if nav_choice == "0":
                                    break
                                elif nav_choice.lower() == "n" and current_page * 10 < len(message_logs):
                                    current_page += 1
                                elif nav_choice.lower() == "p" and current_page > 1:
                                    current_page -= 1
                                    
                        elif log_choice == "2" and config.get('voice_enabled'):  # Call Logs
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
                                    page=current_page,
                                    options_text="\nPress '0' to go back"
                                )
                                nav_choice = self.prompt()
                                if nav_choice == "0":
                                    break
                                elif nav_choice.lower() == "n" and current_page * 10 < len(call_logs):
                                    current_page += 1
                                elif nav_choice.lower() == "p" and current_page > 1:
                                    current_page -= 1

                elif choice == "4":  # Configure Number
                    # Show current config using data from use case
                    config_details = self.manage_flow.get_number_details(self.current_number)
                    options = [
                        "Current Configuration:",
                        f"- Number: {config_details['number']}",
                        f"- Type: {config_details['type'].title()}",
                        f"- Region: {config_details['region']} ({config_details['region_code']})",
                        "",
                        "Available Features:",
                        "✓ Voice" if config.get('voice_enabled') else "✗ Voice not available",
                        "✓ SMS" if config.get('sms_enabled') else "✗ SMS not available",
                        "✓ MMS" if config.get('mms_enabled') else "✗ MMS not available",
                        "✓ Fax" if config.get('fax_enabled') else "✗ Fax not available",
                        "",
                        "Actions:",
                        "1. Configure Voice" if config.get('voice_enabled') else "1. ❌ Voice not available",
                        "2. Configure Messaging" if config.get('sms_enabled') else "2. ❌ Messaging not available",
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
                        
                    # Handle configuration updates
                    if choice == "1" and config.get('voice_enabled'):
                        self.manage_flow.update_number_config(self.current_number, {'voice_enabled': True})
                    elif choice == "2" and config.get('sms_enabled'):
                        self.manage_flow.update_number_config(self.current_number, {'sms_enabled': True})

                elif choice == "5":  # Release Number
                    number_details = self.manage_flow.get_number_details(self.current_number)
                    options = [
                        "Are you sure you want to release this number?",
                        f"{number_details['number']} ({number_details['region']}, {number_details['country_name']})",
                        f"Type: {number_details['type'].title()}, Monthly Cost: ${number_details['price']:.2f}",
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
                        
                    # Release the number using use case
                    if self.manage_flow.release_number(self.current_number):
                        self.show_panel(
                            title="Number Released",
                            subtitle="The number has been released successfully",
                            options=["Press any key to continue"]
                        )
                        self.prompt()
                        break  # Return to number list
                    else:
                        self.show_panel(
                            title="Release Failed",
                            subtitle="Failed to release the number",
                            options=["Press any key to continue"]
                        )
                        self.prompt()