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

    def show_table(self, data, columns, title=None, subtitle=None, page=1, items_per_page=10):
        """
        Display data in a Rich table within a panel with pagination.
        
        Args:
            data: List of dictionaries containing the data
            columns: List of column definitions, each being a dict with 'header' and 'key'
            title: Optional panel title
            subtitle: Optional panel subtitle
            page: Current page number (1-based)
            items_per_page: Number of items to show per page
        """
        from rich.table import Table
        from rich.text import Text
        from rich.panel import Panel
        from rich.console import Group
        
        # Create table with visible borders
        table = Table(show_header=True, header_style="bold magenta")
        
        # Add columns
        for col in columns:
            table.add_column(col['header'], style="cyan")
            
        # Calculate pagination
        start_idx = (page - 1) * items_per_page
        end_idx = start_idx + items_per_page
        page_data = data[start_idx:end_idx]
        total_pages = (len(data) + items_per_page - 1) // items_per_page
        
        # Add rows
        for item in page_data:
            row = [str(item.get(col['key'], '')) for col in columns]
            table.add_row(*row)
            
        # Create navigation text
        nav_text = Text()
        if total_pages > 1:
            nav_text.append(f"\nPage {page} of {total_pages}\n", style="yellow")
            nav_text.append("Navigation: ", style="bold")
            nav_text.append("'n' for next page, 'p' for previous page, 'q' to return")
        
        # Group table and navigation
        group = Group(table, nav_text)
        
        # Create panel title
        title_text = Text(f"[bold red]{title}[/bold red]", justify="center") if title else None
        subtitle_text = Text(f"[bold yellow]{subtitle}[/bold yellow]", justify="center") if subtitle else None
        
        # Create panel with content
        panel = Panel(
            group,
            title=title_text,
            subtitle=subtitle_text,
            border_style="red",
            padding=(1, 8),
            width=80
        )
        
        # Clear console and show panel
        self.console.clear()
        self.console.print(panel)

    def prompt(self, prompt_text="Enter your choice: "):
        """
        Show a prompt below the menu panel.
        """
        return input(prompt_text)
