from app.interfaces.cli.menus.base_menu import BaseMenu

class VoiceConfigMenu(BaseMenu):
    """
    Voice config for a number.
    """
    def show(self):
        options = [
            "1. Configure Voice",
            "0. Back"
        ]
        self.show_panel(
            title="Voice Config",
            subtitle=None,
            options=options
        )
        return self.prompt()
