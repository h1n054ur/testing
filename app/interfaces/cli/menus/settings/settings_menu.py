from app.interfaces.cli.menus.base_menu import BaseMenu

class SettingsMenu(BaseMenu):
    """
    Account settings and admin tools.
    """
    def show(self):
        options = [
            "1. Security Settings",
            "2. Billing Settings",
            "3. Account Logs",
            "4. Subaccounts",
            "5. Developer Tools",
            "6. Advanced Search",
            "7. Diagnostics",
            "8. Config Management",
            "0. Back"
        ]
        self.show_panel(
            title="Settings Menu",
            subtitle="[bold cyan]Account Settings & Admin[/bold cyan]",
            options=options
        )
        return self.prompt()
