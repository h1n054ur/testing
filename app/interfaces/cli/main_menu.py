from app.interfaces.cli.base_menu import BaseMenu
from app.interfaces.cli.purchase_menu import PurchaseMenu
from app.interfaces.cli.manage_menu import ManageMenu
from app.interfaces.cli.settings_menu import SettingsMenu
import sys

class MainMenu(BaseMenu):
    def __init__(self, purchase_flow=None, manage_flow=None, settings_flow=None):
        super().__init__()
        self.purchase_flow = purchase_flow
        self.manage_flow = manage_flow
        self.settings_flow = settings_flow
        
    def show(self):
        try:
            while True:
                options = [
                    "1. Purchase Numbers",
                    "2. Manage Numbers",
                    "3. Settings & Admin",
                    "0. Exit",
                    "",
                    "Press Ctrl+C to exit at any time"
                ]
                self.show_panel(
                    title="TWILIO MANAGER",
                    subtitle="[bold cyan]Main Menu[/bold cyan]",
                    options=options
                )
                try:
                    choice = self.prompt()
                    if choice == "1":
                        PurchaseMenu(purchase_flow=self.purchase_flow).show()
                    elif choice == "2":
                        ManageMenu(manage_flow=self.manage_flow).show()
                    elif choice == "3":
                        SettingsMenu(settings_flow=self.settings_flow).show()
                    elif choice == "0":
                        print("\nExiting.")
                        sys.exit(0)
                    else:
                        print("Invalid selection. Please try again.")
                except SystemExit:
                    # Re-raise SystemExit to properly exit
                    raise
                except Exception as e:
                    print(f"\nAn error occurred: {str(e)}")
                    print("Press Enter to continue or Ctrl+C to exit")
                    self.prompt()
        except KeyboardInterrupt:
            print("\nExiting gracefully...")
            sys.exit(0)
        except Exception as e:
            print(f"\nFatal error: {str(e)}")
            sys.exit(1)
