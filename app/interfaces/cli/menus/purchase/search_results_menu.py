from app.interfaces.cli.menus.base_menu import BaseMenu

class SearchResultsMenu(BaseMenu):
    """
    View and interact with search results (paged).
    """
    def show(self):
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
        return self.prompt()
