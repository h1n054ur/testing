from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.settings.account_logs_menu import AccountLogsMenu
from app.interfaces.cli.menus.settings.advanced_search_menu import AdvancedSearchMenu
from app.interfaces.cli.menus.settings.billing_menu import BillingMenu
from app.interfaces.cli.menus.settings.config_management_menu import ConfigManagementMenu
from app.interfaces.cli.menus.settings.devtools_menu import DevToolsMenu
from app.interfaces.cli.menus.settings.diagnostics_menu import DiagnosticsMenu
from app.interfaces.cli.menus.settings.security_menu import SecurityMenu
from app.interfaces.cli.menus.settings.subaccount_menu import SubaccountMenu

class SettingsMenu(BaseMenu):
    """
    Settings, logs, security, and admin tools.
    """
    def show(self):
        while True:
            options = [
                "1. Usage & Billing",
                "2. Security & Compliance",
                "3. Subaccount Management",
                "4. Developer Tools",
                "5. Account Logs",
                "6. Advanced Search",
                "7. Configuration Management",
                "8. Logs & Diagnostics",
                "0. Back"
            ]
            self.show_panel(
                title="Settings & Admin",
                subtitle="[bold cyan]Settings Menu[/bold cyan]",
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                BillingMenu().show()
            elif choice == "2":
                SecurityMenu().show()
            elif choice == "3":
                SubaccountMenu().show()
            elif choice == "4":
                DevToolsMenu().show()
            elif choice == "5":
                AccountLogsMenu().show()
            elif choice == "6":
                AdvancedSearchMenu().show()
            elif choice == "7":
                ConfigManagementMenu().show()
            elif choice == "8":
                DiagnosticsMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
