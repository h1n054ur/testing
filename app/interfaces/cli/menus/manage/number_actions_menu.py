from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.manage.config_menu import ConfigMenu
from app.interfaces.cli.menus.manage.logs_menu import LogsMenu
from app.interfaces.cli.menus.manage.release_menu import ReleaseMenu

class NumberActionsMenu(BaseMenu):
    """
    Actions for selected number.
    """
    def show(self):
        while True:
            options = [
                "1. Configure Number",
                "2. View Logs",
                "3. Release Number",
                "0. Back"
            ]
            self.show_panel(
                title="Number Actions",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                ConfigMenu().show()
            elif choice == "2":
                LogsMenu().show()
            elif choice == "3":
                ReleaseMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
