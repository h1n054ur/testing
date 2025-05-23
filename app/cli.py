#!/usr/bin/env python3
import argparse
try:
    from app.interfaces.cli.main_menu import MainMenu
    from app.core.manage import ManageFlow
    from app.core.purchase import PurchaseFlow
    from app.core.settings import SettingsFlow
    from app.gateways.twilio_gateway import TwilioGateway
except ImportError:
    print("Error: Some required modules are missing. Please make sure all dependencies are installed.")

def main():
    parser = argparse.ArgumentParser(description='Twilio Manager CLI')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Search commands
    search_parser = subparsers.add_parser('search', help='Search for available phone numbers')
    search_parser.add_argument('--country', required=True, help='Country code (required)')
    search_parser.add_argument('--area-code', help='Area code (optional)')
    search_parser.add_argument('--contains', help='Number contains (optional)')

    # Purchase commands
    purchase_parser = subparsers.add_parser('purchase', help='Purchase a specific phone number')
    purchase_parser.add_argument('number', help='Exact phone number to purchase')
    
    # Manage commands
    manage_parser = subparsers.add_parser('manage', help='Manage phone numbers')
    manage_subparsers = manage_parser.add_subparsers(dest='manage_command')
    
    # SMS commands
    sms_parser = manage_subparsers.add_parser('sms', help='Send SMS')
    sms_parser.add_argument('--from', dest='from_number', required=True, help='From number')
    sms_parser.add_argument('--to', required=True, help='To number')
    sms_parser.add_argument('--message', required=True, help='Message text')

    # Call commands
    call_parser = manage_subparsers.add_parser('call', help='Make calls')
    call_parser.add_argument('--from', dest='from_number', required=True, help='From number')
    call_parser.add_argument('--to', required=True, help='To number')
    
    # Config commands
    config_parser = manage_subparsers.add_parser('config', help='Configure numbers')
    config_parser.add_argument('--number', required=True, help='Phone number to configure')
    config_parser.add_argument('--sms-url', help='SMS webhook URL')
    config_parser.add_argument('--voice-url', help='Voice webhook URL')

    # Settings commands
    settings_parser = subparsers.add_parser('settings', help='Account settings')
    settings_subparsers = settings_parser.add_subparsers(dest='settings_command')
    
    # Account commands
    account_parser = settings_subparsers.add_parser('account', help='Account management')
    account_parser.add_argument('--show-balance', action='store_true', help='Show account balance')
    account_parser.add_argument('--show-numbers', action='store_true', help='List all numbers')

    # Logs commands
    logs_parser = settings_subparsers.add_parser('logs', help='View logs')
    logs_parser.add_argument('--type', choices=['sms', 'call', 'all'], default='all', help='Log type')
    logs_parser.add_argument('--limit', type=int, default=50, help='Number of logs to show')

    args = parser.parse_args()

    # Initialize Twilio gateway
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    
    if not account_sid or not auth_token:
        print("Error: Missing Twilio credentials")
        print("Please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN in .env file")
        return
    
    twilio_gateway = TwilioGateway(account_sid, auth_token)

    if not args.command:
        # Launch interactive menu
        purchase = PurchaseFlow(twilio_gateway=twilio_gateway)
        manage = ManageFlow(twilio_gateway=twilio_gateway)
        settings = SettingsFlow(twilio_gateway=twilio_gateway)
        MainMenu(purchase=purchase, manage=manage, settings=settings).show()
        return

    # Handle CLI commands
    if args.command == 'search':
        flow = PurchaseFlow(twilio_gateway=twilio_gateway)
        # Display progress in CLI
        def progress_callback(count):
            print(f"\rFound {count} numbers...", end="")

        # Search for numbers
        results = flow.search_numbers(args.country, "local", args.area_code, args.contains, progress_callback)
        print("\n")  # New line after progress

        # Display results
        if results:
            print(f"Found {len(results)} available numbers:")
            for result in results:
                print(f"{result['index']}. {result['number']} - {result['city']}, {result['state']} - {result['type']} - {result['price']}")
        else:
            print("No numbers found.")

    elif args.command == 'purchase':
        flow = PurchaseFlow(twilio_gateway=twilio_gateway)
        result = flow.purchase_exact_number(args.number)
        if result.get("success"):
            print(f"Success: {result['message']}")
        else:
            print(f"Error: {result['message']}")
    
    elif args.command == 'manage':
        flow = ManageFlow(twilio_gateway=twilio_gateway)
        if args.manage_command == 'sms':
            result = flow.send_sms(args.from_number, args.to, args.message)
            if result.get("success"):
                print("SMS sent successfully!")
            else:
                print(f"Error sending SMS: {result.get('error', 'Unknown error')}")
        elif args.manage_command == 'call':
            result = flow.make_call(args.from_number, args.to)
            if result.get("success"):
                print("Call initiated successfully!")
            else:
                print(f"Error making call: {result.get('error', 'Unknown error')}")
        elif args.manage_command == 'config':
            flow.configure_number(args.number, args.sms_url, args.voice_url)
    
    elif args.command == 'settings':
        flow = SettingsFlow(twilio_gateway=twilio_gateway)
        if args.settings_command == 'account':
            if args.show_balance:
                flow.show_balance()
            if args.show_numbers:
                numbers = flow.twilio_gateway.list_active_numbers()
                if numbers.get("success"):
                    print("\nManaged Numbers:")
                    for number in numbers.get("numbers", []):
                        capabilities = [cap for cap, enabled in number["capabilities"].items() if enabled]
                        print(f"  {number['number']} (Capabilities: {', '.join(capabilities)})")
                else:
                    print(f"Error listing numbers: {numbers.get('error', 'Unknown error')}")
        elif args.settings_command == 'logs':
            flow.view_logs(args.type, args.limit)

if __name__ == '__main__':
    main()