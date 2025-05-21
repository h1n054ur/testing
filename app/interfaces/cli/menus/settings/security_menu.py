from app.interfaces.cli.menus.base_menu import BaseMenu

class SecurityMenu(BaseMenu):
    """
    Security and compliance settings.
    """
    def show(self):
        options = [
            "1. Authentication",
            "2. API Keys",
            "3. Compliance",
            "4. Audit Logs",
            "0. Back"
        ]
        self.show_panel(
            title="Security Menu",
            subtitle=None,
            options=options
        )
        return self.prompt()
