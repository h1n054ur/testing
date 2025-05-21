from app.interfaces.cli.menus.base_menu import BaseMenu

class PurchaseConfirmMenu(BaseMenu):
    """
    Confirm before purchase.
    """
    def show(self):
        options = [
            "1. Confirm Purchase",
            "0. Back"
        ]
        self.show_panel(
            title="Confirm Purchase",
            subtitle=None,
            options=options
        )
        return self.prompt()
