from app.interfaces.cli.menus.base_menu import BaseMenu

class NumberActionsMenu(BaseMenu):
    """
    Actions for selected number.
    """
    def show(self):
        options = [
            "1. Configure Number",
            "2. View Call Logs",
            "3. View Message Logs",
            "4. Release Number",
            "0. Back"
        ]
        self.show_panel(
            title="Number Actions",
            subtitle=None,
            options=options
        )
        return self.prompt()
