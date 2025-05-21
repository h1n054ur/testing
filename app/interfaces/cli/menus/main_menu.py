from app.interfaces.cli.menus.base_menu import BaseMenu

class MainMenu(BaseMenu):
    """
    Main entry menu. "0. Exit" quits app.
    """
    def show(self):
        options = [
            "1. Purchase Numbers",
            "2. Manage Numbers", 
            "3. Settings & Admin",
            "0. Exit"
        ]
        self.show_panel(
            title="TWILIO MANAGER",
            subtitle="Subaccount: Default\n[bold cyan]Main Menu[/bold cyan]",
            options=options
        )
        return self.prompt()
