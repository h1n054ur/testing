from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.purchase.locality_input_menu import LocalityInputMenu

class PurchaseMenu(BaseMenu):
    """
    Guided flow: select country, type, search mode, capabilities, begin search, view/purchase.
    """
    def show(self):
        while True:
            options = [
                "1. Start Number Search",
                "0. Back"
            ]
            self.show_panel(
                title="Purchase Numbers",
                subtitle="[bold cyan]Purchase Menu[/bold cyan]",
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                LocalityInputMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
