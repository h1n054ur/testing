from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.purchase.search_results_menu import SearchResultsMenu

class SearchProgressMenu(BaseMenu):
    """
    Displays spinner while searching numbers.
    """
    def show(self):
        self.show_panel(
            title="Searching Numbers",
            subtitle="[bold yellow]Searching, please wait...[/bold yellow]",
            options=None
        )
        self.show_spinner(text="Searching available numbers")
        input("Press Enter to continue...")
        SearchResultsMenu().show()
