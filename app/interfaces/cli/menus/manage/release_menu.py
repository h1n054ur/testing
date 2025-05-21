from app.interfaces.cli.menus.base_menu import BaseMenu

class ReleaseMenu(BaseMenu):
    """
    Confirm release of selected number.
    """
    def show(self):
        while True:
            options = [
                "1. Confirm Release",
                "0. Back"
            ]
            self.show_panel(
                title="Release Number",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                # In future: perform release action
                print("Number released! (stub)")
                return
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
