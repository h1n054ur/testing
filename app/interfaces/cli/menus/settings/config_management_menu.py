from app.interfaces.cli.menus.base_menu import BaseMenu

class ConfigManagementMenu(BaseMenu):
    """
    Manage system and number configs.
    """
    def show(self):
        while True:
            options = [
                "1. System Settings",
                "2. Number Settings",
                "3. Import Config",
                "4. Export Config",
                "0. Back"
            ]
            self.show_panel(
                title="Config Management",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
