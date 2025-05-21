from app.interfaces.cli.menus.base_menu import BaseMenu

class LocalityInputMenu(BaseMenu):
    """
    Menu for locality/region input during number search.
    """
    def show(self):
        options = [
            "1. Enter Locality Name",
            "0. Back"
        ]
        self.show_panel(
            title="Number Search: Locality",
            subtitle=None,
            options=options
        )
        return self.prompt()
