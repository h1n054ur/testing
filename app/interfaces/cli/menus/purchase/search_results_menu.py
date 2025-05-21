from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.purchase.purchase_confirm_menu import PurchaseConfirmMenu

class SearchResultsMenu(BaseMenu):
    """
    View and interact with search results (paged).
    """
    def show(self):
        while True:
            options = [
                "n. Next Page",
                "p. Previous Page",
                "s. Sort",
                "j. Save to JSON",
                "c. Save to CSV",
                "x. Select number(s) to purchase",
                "0. Back"
            ]
            self.show_panel(
                title="Search Results",
                subtitle="[bold cyan]Results[/bold cyan]",
                options=options
            )
            choice = self.prompt()
            if choice == "x":
                PurchaseConfirmMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
