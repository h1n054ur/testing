from app.interfaces.cli.menus.base_menu import BaseMenu

class BillingMenu(BaseMenu):
    """
    View billing and usage.
    """
    def show(self):
        options = [
            "1. View Usage",
            "2. View Bills",
            "3. Payment Methods",
            "4. Billing Settings",
            "0. Back"
        ]
        self.show_panel(
            title="Billing Menu",
            subtitle=None,
            options=options
        )
        return self.prompt()
