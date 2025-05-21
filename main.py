from app.interfaces.cli.main_menu import MainMenu
from app.models.country_data import country_data
from app.use_cases.purchase_flow import PurchaseFlow
from app.use_cases.manage_flow import ManageFlow
from app.use_cases.settings_flow import SettingsFlow

def main():
    # Initialize use cases with country_data
    purchase_flow = PurchaseFlow()
    manage_flow = ManageFlow()
    settings_flow = SettingsFlow()
    
    # Initialize main menu with use cases
    MainMenu(
        purchase_flow=purchase_flow,
        manage_flow=manage_flow,
        settings_flow=settings_flow
    ).show()

if __name__ == "__main__":
    main()
