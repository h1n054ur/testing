from app.interfaces.cli.menus.base_menu import BaseMenu

class AccountLogsMenu(BaseMenu):
    """
    View account-wide logs.
    """
    def show(self):
        options = [
            "1. View All Logs",
            "2. Filter by Date",
            "3. Filter by Type",
            "4. Export Logs",
            "0. Back"
        ]
        self.show_panel(
            title="Account Logs",
            subtitle=None,
            options=options
        )
        return self.prompt()
