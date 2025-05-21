from app.interfaces.cli.menus.base_menu import BaseMenu

class DevToolsMenu(BaseMenu):
    """
    Developer tools and diagnostics.
    """
    def show(self):
        options = [
            "1. API Console",
            "2. Debug Logs",
            "3. Test Tools",
            "4. Performance",
            "0. Back"
        ]
        self.show_panel(
            title="Developer Tools",
            subtitle=None,
            options=options
        )
        return self.prompt()
