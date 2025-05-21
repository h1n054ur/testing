from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.spinner import Spinner

class BaseMenu:
    """
    Base class for all CLI menus. Handles Rich-based menu display, box styling,
    centering, and sectioning. All menus must inherit from this and call self.show_panel().
    """
    console = Console()

    def show_panel(self, title, subtitle=None, options=None):
        """
        Render a styled menu panel with a title, subtitle, and list of options.
        Title and subtitle are centered; options are visually padded to appear centered.
        """
        lines = []
        if subtitle:
            lines.append(f"[bold yellow]{subtitle}[/bold yellow]\n")
        if options:
            pad = max(len(opt) for opt in options)
            for opt in options:
                lines.append(f"  {opt.ljust(pad)}  ")
        content = "\n".join(lines)
        panel = Panel(
            Align.center(content, vertical="middle"),
            title=f"[bold orange1]{title}[/bold orange1]",
            border_style="orange1",
            padding=(1, 4)
        )
        self.console.clear()
        self.console.print(panel)

    def show_spinner(self, text="Searching..."):
        """
        Show a Rich spinner for loading/processing steps.
        """
        with self.console.status(f"[bold green]{text}[/bold green]", spinner="dots"):
            import time
            time.sleep(2)  # Simulate search (replace with real logic later)

    def prompt(self, prompt_text="Enter your choice: "):
        """
        Show a prompt below the menu panel.
        """
        return input(prompt_text)
