from app.interfaces.cli.menus.base_menu import BaseMenu

class ConfigMenu(BaseMenu):
    """
    Configure selected phone number.
    """
    def show(self):
        options = [
            "1. Configure Number",
            "0. Back"
        ]
        self.show_panel(
            title="Configure Number",
            subtitle=None,
            options=options
        )
        return self.prompt()
