from app.interfaces.cli.base_menu import BaseMenu
from app.core.manage import ManageFlow

class ManageMenu(BaseMenu):
    def __init__(self, manage=None):
        super().__init__()
        self.manage = manage or ManageFlow()
        self.current_number = None

    def show(self):
        while True:
            # Step 2.1: View Active Numbers
            active_numbers = self.manage.get_managed_numbers()
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
                # Get number details from core module
                number_details = self.manage.get_number_details(self.current_number)
                if not number_details:
                    print("Error: Number details not found")
                    break
                    
                # Get available configurations
                config = self.manage.get_available_configurations(self.current_number)
                
                options = [
                    f"Selected: {number_details['number']} ({number_details['region']}, {number_details['country_name']})",
                    f"Type: {number_details['type'].title()}, Monthly Cost: ${number_details['price']:.2f}",
                    "",
                    "1. Make a Call" if config.get('voice_enabled') else "1. [X] Voice not available",
                    "2. Send an SMS" if config.get('sms_enabled') else "2. [X] SMS not available",
                    "3. View Logs",
                    "4. Configure Number",
                    "5. Release Number",
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
                    # Get destination number
                    self.show_panel(
                        title="Make a Call",
                        subtitle="Enter destination number",
                        options=["Enter destination number (e.g. +1234567890):", "0. Back"]
                    )
                    to_number = self.prompt()
                    if to_number == "0":
                        continue

                    # Basic TwiML for a simple voice call
                    twiml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Hello! This is a test call from your Twilio Manager.</Say>
    <Pause length="1"/>
    <Say>Goodbye!</Say>
</Response>"""

                    # Make the call via gateway
                    result = self.manage.make_call(self.current_number, to_number, twiml)
                    
                    if result["success"]:
                        self.show_panel(
                            title="Call Initiated",
                            subtitle=f"Call to {to_number} has been started",
                            options=[
                                f"Status: {result['status']}",
                                f"Call SID: {result['sid']}",
                                "",
                                "Press any key to continue"
                            ]
                        )
                    else:
                        self.show_panel(
                            title="Call Failed",
                            subtitle="Failed to initiate call",
                            options=[
                                f"Error: {result['error']}",
                                "",
                                "Press any key to continue"
                            ]
                        )
                    self.prompt()

                elif choice == "2" and config.get('sms_enabled'):  # Send an SMS
                    # Get destination number
                    self.show_panel(
                        title="Send SMS",
                        subtitle="Enter destination number",
                        options=["Enter destination number (e.g. +1234567890):", "0. Back"]
                    )
                    to_number = self.prompt()
                    if to_number == "0":
                        continue

                    # Get message text
                    self.show_panel(
                        title="Send SMS",
                        subtitle="Enter message text",
                        options=["Type your message:", "0. Back"]
                    )
                    message = self.prompt()
                    if message == "0":
                        continue

                    # Send SMS via gateway
                    result = self.manage.send_sms(self.current_number, to_number, message)
                    
                    if result["success"]:
                        self.show_panel(
                            title="SMS Sent",
                            subtitle=f"Message to {to_number} has been sent",
                            options=[
                                f"Status: {result['status']}",
                                f"Message SID: {result['sid']}",
                                "",
                                "Press any key to continue"
                            ]
                        )
                    else:
                        self.show_panel(
                            title="SMS Failed",
                            subtitle="Failed to send message",
                            options=[
                                f"Error: {result['error']}",
                                "",
                                "Press any key to continue"
                            ]
                        )
                    self.prompt()

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
                            # Get real message logs from use case
                            message_logs = self.manage.get_message_logs(self.current_number)
                            
                            if not message_logs:
                                self.show_panel(
                                    title="No Messages",
                                    subtitle="No message history found",
                                    options=["Press any key to go back"]
                                )
                                self.prompt()
                                continue
                            
                            columns = [
                                {"header": "Date", "key": "date"},
                                {"header": "Direction", "key": "direction"},
                                {"header": "From", "key": "from"},
                                {"header": "To", "key": "to"},
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
                            # Get real call logs from use case
                            call_logs = self.manage.get_call_logs(self.current_number)
                            
                            if not call_logs:
                                self.show_panel(
                                    title="No Calls",
                                    subtitle="No call history found",
                                    options=["Press any key to go back"]
                                )
                                self.prompt()
                                continue
                            
                            columns = [
                                {"header": "Date", "key": "date"},
                                {"header": "Direction", "key": "direction"},
                                {"header": "From", "key": "from"},
                                {"header": "To", "key": "to"},
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
                    config_details = self.manage.get_number_details(self.current_number)
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
                        
                    # Handle configuration updates
                    if choice == "1" and config.get('voice_enabled'):
                        # Configure voice
                        options = [
                            "1. Set Voice URL",
                            "2. Set Voice Method (GET/POST)",
                            "3. Set Voice Fallback URL",
                            "4. Set Status Callback URL",
                            "0. Back"
                        ]
                        self.show_panel(
                            title="Configure Voice",
                            subtitle="Voice settings for " + self.current_number,
                            options=options
                        )
                        voice_choice = self.prompt()
                        if voice_choice == "1":
                            self.show_panel(
                                title="Set Voice URL",
                                subtitle="Enter the URL that Twilio should request when this number receives a call",
                                options=["Enter URL:", "0. Back"]
                            )
                            url = self.prompt()
                            if url != "0":
                                result = self.manage.configure_voice(self.current_number, 'voice_url', url)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                        elif voice_choice == "2":
                            self.show_panel(
                                title="Set Voice Method",
                                subtitle="Choose HTTP method for voice URL requests",
                                options=["1. GET", "2. POST", "0. Back"]
                            )
                            method_choice = self.prompt()
                            if method_choice in ["1", "2"]:
                                method = "GET" if method_choice == "1" else "POST"
                                result = self.manage.configure_voice(self.current_number, 'voice_method', method)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                        elif voice_choice == "3":
                            self.show_panel(
                                title="Set Voice Fallback URL",
                                subtitle="Enter the URL that Twilio should request if the primary URL fails",
                                options=["Enter URL:", "0. Back"]
                            )
                            url = self.prompt()
                            if url != "0":
                                result = self.manage.configure_voice(self.current_number, 'voice_fallback_url', url)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                        elif voice_choice == "4":
                            self.show_panel(
                                title="Set Status Callback URL",
                                subtitle="Enter the URL for call status updates",
                                options=["Enter URL:", "0. Back"]
                            )
                            url = self.prompt()
                            if url != "0":
                                result = self.manage.configure_voice(self.current_number, 'status_callback', url)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")

                    elif choice == "2" and config.get('sms_enabled'):
                        # Configure messaging
                        options = [
                            "1. Set SMS URL",
                            "2. Set SMS Method (GET/POST)",
                            "3. Set SMS Fallback URL",
                            "4. Set SMS Status Callback",
                            "0. Back"
                        ]
                        self.show_panel(
                            title="Configure Messaging",
                            subtitle="SMS settings for " + self.current_number,
                            options=options
                        )
                        sms_choice = self.prompt()
                        if sms_choice == "1":
                            self.show_panel(
                                title="Set SMS URL",
                                subtitle="Enter the URL that Twilio should request when this number receives a message",
                                options=["Enter URL:", "0. Back"]
                            )
                            url = self.prompt()
                            if url != "0":
                                result = self.manage.configure_messaging(self.current_number, 'sms_url', url)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                        elif sms_choice == "2":
                            self.show_panel(
                                title="Set SMS Method",
                                subtitle="Choose HTTP method for SMS URL requests",
                                options=["1. GET", "2. POST", "0. Back"]
                            )
                            method_choice = self.prompt()
                            if method_choice in ["1", "2"]:
                                method = "GET" if method_choice == "1" else "POST"
                                result = self.manage.configure_messaging(self.current_number, 'sms_method', method)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                        elif sms_choice == "3":
                            self.show_panel(
                                title="Set SMS Fallback URL",
                                subtitle="Enter the URL that Twilio should request if the primary URL fails",
                                options=["Enter URL:", "0. Back"]
                            )
                            url = self.prompt()
                            if url != "0":
                                result = self.manage.configure_messaging(self.current_number, 'sms_fallback_url', url)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                        elif sms_choice == "4":
                            self.show_panel(
                                title="Set SMS Status Callback",
                                subtitle="Enter the URL for message status updates",
                                options=["Enter URL:", "0. Back"]
                            )
                            url = self.prompt()
                            if url != "0":
                                result = self.manage.configure_messaging(self.current_number, 'sms_status_callback', url)
                                if not result.get("success"):
                                    print(f"\nError: {result.get('error', 'Unknown error')}")
                                    
                    elif choice == "3":  # Set Friendly Name
                        self.show_panel(
                            title="Set Friendly Name",
                            subtitle="Enter a friendly name for " + self.current_number,
                            options=["Enter friendly name:", "0. Back"]
                        )
                        friendly_name = self.prompt()
                        if friendly_name != "0":
                            result = self.manage.set_friendly_name(self.current_number, friendly_name)
                            if not result.get("success"):
                                print(f"\nError: {result.get('error', 'Unknown error')}")

                elif choice == "5":  # Release Number
                    number_details = self.manage.get_number_details(self.current_number)
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
                    if self.manage.release_number(self.current_number):
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