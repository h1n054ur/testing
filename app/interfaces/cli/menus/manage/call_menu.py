from app.interfaces.cli.menus.base_menu import BaseMenu

class CallMenu(BaseMenu):
    """
    Voice call options for a selected number.
    """
    def show(self):
        options = [
            "1. Make Call",
            "0. Back"
        ]
        self.show_panel(
            title="Call Menu",
            subtitle=None,
            options=options
        )
        return self.prompt()
