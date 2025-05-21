from app.interfaces.cli.menus.base_menu import BaseMenu

class AdvancedSearchMenu(BaseMenu):
    """
    Advanced number search options.
    """
    def show(self):
        while True:
            options = [
                "1. Search by Pattern",
                "2. Search by Features",
                "3. Search by Region",
                "4. Save Search",
                "0. Back"
            ]
            self.show_panel(
                title="Advanced Search",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
