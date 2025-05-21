from app.interfaces.cli.menus.base_menu import BaseMenu

class LogsMenu(BaseMenu):
    """
    View message and call logs for a number.
    """
    def show(self):
        options = [
            "1. Messaging Logs",
            "2. Call Logs",
            "0. Back"
        ]
        self.show_panel(
            title="Logs Menu",
            subtitle=None,
            options=options
        )
        return self.prompt()
