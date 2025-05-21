from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.purchase.purchase_menu import PurchaseMenu
from app.interfaces.cli.menus.manage.manage_menu import ManageMenu
from app.interfaces.cli.menus.settings.settings_menu import SettingsMenu
import sys

class MainMenu(BaseMenu):
    """
    Main entry menu. "0. Exit" quits app.
    """
    def show(self):
        while True:
            options = [
                "1. Purchase Numbers",
                "2. Manage Numbers",
                "3. Settings & Admin",
                "0. Exit"
            ]
            self.show_panel(
                title="TWILIO MANAGER",
                subtitle="Subaccount: Default\n[bold cyan]Main Menu[/bold cyan]",
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                PurchaseMenu().show()
            elif choice == "2":
                ManageMenu().show()
            elif choice == "3":
                SettingsMenu().show()
            elif choice == "0":
                print("Exiting Twilio Manager CLI.")
                sys.exit(0)
            else:
                print("Invalid selection. Please try again.")
