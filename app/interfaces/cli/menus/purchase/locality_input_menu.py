from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.purchase.search_progress_menu import SearchProgressMenu

class LocalityInputMenu(BaseMenu):
    """
    Menu for locality/region input during number search.
    """
    def show(self):
        while True:
            options = [
                "1. Begin Search",
                "0. Back"
            ]
            self.show_panel(
                title="Number Search: Locality",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                SearchProgressMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
