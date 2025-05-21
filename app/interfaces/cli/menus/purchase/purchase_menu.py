from app.interfaces.cli.menus.base_menu import BaseMenu

class PurchaseMenu(BaseMenu):
    """
    Guided flow: select country, type, search mode, capabilities, begin search, view/purchase.
    """
    def show(self):
        options = [
            "1. Start Number Search",
            "0. Back"
        ]
        self.show_panel(
            title="Purchase Numbers",
            subtitle="[bold cyan]Purchase Menu[/bold cyan]",
            options=options
        )
        return self.prompt()
