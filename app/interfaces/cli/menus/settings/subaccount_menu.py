from app.interfaces.cli.menus.base_menu import BaseMenu

class SubaccountMenu(BaseMenu):
    """
    Manage Twilio subaccounts.
    """
    def show(self):
        options = [
            "1. View Subaccounts",
            "2. Create Subaccount",
            "3. Manage Access",
            "4. Delete Subaccount",
            "0. Back"
        ]
        self.show_panel(
            title="Subaccount Menu",
            subtitle=None,
            options=options
        )
        return self.prompt()
