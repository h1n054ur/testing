from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.manage.sms_menu import SMSMenu
from app.interfaces.cli.menus.manage.call_menu import CallMenu

class LogsMenu(BaseMenu):
    """
    View message and call logs for a number.
    """
    def show(self):
        while True:
            options = [
                "1. Messaging Logs",
                "2. Call Logs",
                "0. Back"
            ]
            self.show_panel(
                title="Logs Menu",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                SMSMenu().show()
            elif choice == "2":
                CallMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
