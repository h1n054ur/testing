from app.interfaces.cli.menus.base_menu import BaseMenu

class SMSMenu(BaseMenu):
    """
    Send/view SMS for a number.
    """
    def show(self):
        options = [
            "1. Send SMS",
            "2. View SMS Logs",
            "0. Back"
        ]
        self.show_panel(
            title="SMS Menu",
            subtitle=None,
            options=options
        )
        return self.prompt()
