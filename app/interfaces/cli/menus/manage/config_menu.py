from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.manage.messaging_config_menu import MessagingConfigMenu
from app.interfaces.cli.menus.manage.voice_config_menu import VoiceConfigMenu

class ConfigMenu(BaseMenu):
    """
    Configure selected phone number.
    """
    def show(self):
        while True:
            options = [
                "1. Messaging Configuration",
                "2. Voice Configuration",
                "0. Back"
            ]
            self.show_panel(
                title="Configure Number",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                MessagingConfigMenu().show()
            elif choice == "2":
                VoiceConfigMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
