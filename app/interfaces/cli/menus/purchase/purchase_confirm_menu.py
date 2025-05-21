from app.interfaces.cli.menus.base_menu import BaseMenu

class PurchaseConfirmMenu(BaseMenu):
    """
    Confirm before purchase.
    """
    def show(self):
        while True:
            options = [
                "1. Confirm Purchase",
                "0. Back"
            ]
            self.show_panel(
                title="Confirm Purchase",
                subtitle=None,
                options=options
            )
            choice = self.prompt()
            if choice == "1":
                # In future: perform purchase action
                print("Purchase confirmed! (stub)")
                return
            elif choice == "0":
                return
            else:
                print("Invalid selection. Please try again.")
