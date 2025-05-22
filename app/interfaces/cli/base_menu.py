from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.spinner import Spinner

class BaseMenu:
    console = Console()

    def show_panel(self, title, subtitle=None, options=None):
        lines = []
        # Main title is always TWILIO MANAGER
        title_text = Text("TWILIO MANAGER", justify="center", style="bold white")
        
        # Add original title as yellow subtitle if it's not TWILIO MANAGER
        if title and title != "TWILIO MANAGER":
            lines.append(Text(title, justify="center", style="yellow bold"))
            lines.append(Text(""))  # Empty line after subtitle
            
        if subtitle:
            lines.append(Text(subtitle, justify="center", style="yellow"))
            lines.append(Text(""))  # Empty line after subtitle
            
        if options:
            for opt in options:
                # Handle rich text markup if present
                if isinstance(opt, str) and "[" in opt and "]" in opt:
                    lines.append(Text.from_markup(opt, justify="center"))
                else:
                    lines.append(Text(opt, justify="center"))
                    
        content = "\n".join(str(l) for l in lines)
        
        # Use wider panel during search and results
        panel_width = 100 if any(x in str(title) for x in ["Searching Numbers", "Search Results"]) else 50
        panel = Panel(
            content,
            title=title_text,
            border_style="red",
            padding=(1, 8),
            width=panel_width
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

    def show_table(self, data, columns, title=None, subtitle=None, page=1, items_per_page=10, options_text=None):
        """
        Display data in a Rich table within a panel with pagination.
        
        Args:
            data: List of dictionaries containing the data
            columns: List of column definitions, each being a dict with 'header' and 'key'
            title: Optional panel title
            subtitle: Optional panel subtitle
            page: Current page number (1-based)
            items_per_page: Number of items to show per page
            options_text: Optional text to display below the table showing available options
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
            
        # Create footer text (navigation + options)
        footer_text = Text()
        
        # Add pagination info if multiple pages
        if total_pages > 1:
            footer_text.append(f"\nPage {page} of {total_pages}\n", style="yellow")
            footer_text.append("Navigation: ", style="bold")
            footer_text.append("'n' for next page, 'p' for previous page, 'q' to return\n")
        
        # Add options text if provided
        if options_text:
            if total_pages > 1:  # Add extra newline if we had pagination
                footer_text.append("\n")
            footer_text.append(options_text)
        
        # Group table and footer
        group = Group(table, footer_text)
        
        # Main title is always TWILIO MANAGER
        title_text = Text("TWILIO MANAGER", justify="center", style="bold white")
        
        # Create a group with title, subtitle, and content
        elements = []
        
        # Add original title as yellow subtitle if it's not TWILIO MANAGER
        if title and title != "TWILIO MANAGER":
            elements.append(Text(title, justify="center", style="yellow bold"))
            elements.append(Text(""))  # Empty line
            
        if subtitle:
            elements.append(Text(subtitle, justify="center", style="yellow"))
            elements.append(Text(""))  # Empty line
            
        elements.append(table)
        elements.append(Text(""))  # Empty line
        elements.append(footer_text)
        
        content_group = Group(*elements)
        
        # Create panel with content
        panel = Panel(
            content_group,
            title=title_text,
            border_style="red",
            padding=(1, 8),
            width=100
        )
        
        # Clear console and show panel
        self.console.clear()
        self.console.print(panel)

    def prompt(self, prompt_text="Enter your choice: "):
        """
        Show a prompt below the menu panel.
        """
        return input(prompt_text)
