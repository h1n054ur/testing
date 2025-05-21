from app.interfaces.cli.menus.base_menu import BaseMenu

class ManageMenu(BaseMenu):
    """
    View, select, manage active numbers.
    """
    def show(self):
        options = [
            "1. View Active Numbers",
            "0. Back"
        ]
        self.show_panel(
            title="Manage Numbers",
            subtitle="[bold cyan]Active Numbers[/bold cyan]",
            options=options
        )
        return self.prompt()
