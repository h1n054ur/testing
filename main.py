import os
import sys
from dotenv import load_dotenv

from app.interfaces.cli.main_menu import MainMenu
from app.models.country_data import country_data
from app.core.purchase import PurchaseFlow
from app.core.manage import ManageFlow
from app.core.settings import SettingsFlow
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
    
    # Initialize core modules with gateway
    purchase = PurchaseFlow(twilio_gateway=twilio_gateway)
    manage = ManageFlow(twilio_gateway=twilio_gateway)
    settings = SettingsFlow(twilio_gateway=twilio_gateway)
    
    # Initialize main menu with core modules
    MainMenu(
        purchase=purchase,
        manage=manage,
        settings=settings
    ).show()

if __name__ == "__main__":
    main()
