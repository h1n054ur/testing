import os
import sys
from dotenv import load_dotenv

from app.interfaces.cli.main_menu import MainMenu
from app.models.country_data import country_data
from app.use_cases.purchase_flow import PurchaseFlow
from app.use_cases.manage_flow import ManageFlow
from app.use_cases.settings_flow import SettingsFlow
from app.gateways.twilio_gateway import TwilioGateway

def main():
    # Load environment variables
    load_dotenv()
    
    # Get Twilio credentials
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    
    if not account_sid or not auth_token:
        print("Error: Missing Twilio credentials")
        print("Please set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN in .env file")
        sys.exit(1)
    
    # Initialize Twilio gateway
    twilio_gateway = TwilioGateway(account_sid, auth_token)
    
    # Initialize use cases with country_data and gateway
    purchase_flow = PurchaseFlow(twilio_gateway=twilio_gateway)
    manage_flow = ManageFlow(twilio_gateway=twilio_gateway)
    settings_flow = SettingsFlow(twilio_gateway=twilio_gateway)
    
    # Initialize main menu with use cases
    MainMenu(
        purchase_flow=purchase_flow,
        manage_flow=manage_flow,
        settings_flow=settings_flow
    ).show()

if __name__ == "__main__":
    main()
