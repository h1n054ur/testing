from app.interfaces.cli.menus.base_menu import BaseMenu

class DiagnosticsMenu(BaseMenu):
    """
    System health and diagnostics.
    """
    def show(self):
        options = [
            "1. Health Check",
            "2. System Info",
            "3. Debug Info",
            "4. Run Tests",
            "0. Back"
        ]
        self.show_panel(
            title="Diagnostics",
            subtitle=None,
            options=options
        )
        return self.prompt()
