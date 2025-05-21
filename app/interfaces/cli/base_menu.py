from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.spinner import Spinner

class BaseMenu:
    console = Console()

    def show_panel(self, title, subtitle=None, options=None):
        lines = []
        if subtitle:
            lines.append(Text(f"[bold yellow]{subtitle}[/bold yellow]", justify="center"))
        if options:
            for opt in options:
                lines.append(Text(opt, justify="center"))
        content = "\n".join(str(l) for l in lines)
        title_text = Text(f"[bold red]{title}[/bold red]", justify="center")
        panel = Panel(
            content,
            title=title_text,
            border_style="red",
            padding=(1, 8),
            width=50
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
