from app.interfaces.cli.menus.base_menu import BaseMenu

class MessagingConfigMenu(BaseMenu):
    """
    SMS/MMS config for a number.
    """
    def show(self):
        options = [
            "1. Configure Messaging",
            "0. Back"
        ]
        self.show_panel(
            title="Messaging Config",
            subtitle=None,
            options=options
        )
        return self.prompt()
