#!/usr/bin/env python3
import argparse
try:
    from app.interfaces.cli.menus.main_menu import MainMenu
    from app.use_cases.manage_flow import ManageFlow
    from app.use_cases.purchase_flow import PurchaseFlow
    from app.use_cases.settings_flow import SettingsFlow
except ImportError:
    print("Error: Some required modules are missing. Please make sure all dependencies are installed.")

def main():
    parser = argparse.ArgumentParser(description='Twilio Manager CLI')
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Purchase commands
    purchase_parser = subparsers.add_parser('purchase', help='Purchase phone numbers')
    purchase_parser.add_argument('--country', help='Country code')
    purchase_parser.add_argument('--area-code', help='Area code')
    purchase_parser.add_argument('--contains', help='Number contains')
    
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

    if not args.command or args.command == 'menu':
        # Launch interactive menu
        MainMenu().display()
        return

    # Handle CLI commands
    if args.command == 'purchase':
        flow = PurchaseFlow()
        flow.search_numbers(args.country, args.area_code, args.contains)
    
    elif args.command == 'manage':
        flow = ManageFlow()
        if args.manage_command == 'sms':
            flow.send_sms(args.from_number, args.to, args.message)
        elif args.manage_command == 'call':
            flow.make_call(args.from_number, args.to)
        elif args.manage_command == 'config':
            flow.configure_number(args.number, args.sms_url, args.voice_url)
    
    elif args.command == 'settings':
        flow = SettingsFlow()
        if args.settings_command == 'account':
            if args.show_balance:
                flow.show_balance()
            if args.show_numbers:
                flow.list_numbers()
        elif args.settings_command == 'logs':
            flow.view_logs(args.type, args.limit)

if __name__ == '__main__':
    main()