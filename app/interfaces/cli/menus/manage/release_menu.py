from app.interfaces.cli.menus.base_menu import BaseMenu

class ReleaseMenu(BaseMenu):
    """
    Confirm release of selected number.
    """
    def show(self):
        options = [
            "1. Confirm Release",
            "0. Back"
        ]
        self.show_panel(
            title="Release Number",
            subtitle=None,
            options=options
        )
        return self.prompt()
