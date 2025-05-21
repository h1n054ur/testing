from app.interfaces.cli.menus.base_menu import BaseMenu

class DevToolsMenu(BaseMenu):
    """
    Developer tools and diagnostics.
    """
    def show(self):
        while True:
            options = [
                "1. API Console",
                "2. Debug Logs",
                "3. Test Tools",
                "4. Performance",
                "0. Back"
            ]
            self.show_panel(
                title="Developer Tools",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
