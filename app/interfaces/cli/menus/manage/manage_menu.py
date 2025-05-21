from app.interfaces.cli.menus.base_menu import BaseMenu
from app.interfaces.cli.menus.manage.number_actions_menu import NumberActionsMenu

class ManageMenu(BaseMenu):
    """
    View, select, manage active numbers.
    """
    def show(self):
        while True:
            options = [
                "1. Select Number (stub)",
                "0. Back"
            ]
            self.show_panel(
                title="Manage Numbers",
                subtitle="[bold cyan]Active Numbers[/bold cyan]",
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                NumberActionsMenu().show()
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
