# import pyfiglet  # !!!!!!!!!!!

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text


console = Console()

# intro slide
intro_markdown_content = """
# Udemy Python Mock, patch and monkeypatch

- Craig West
- Community first person 💛

"""

# What is Rich?
basics_markdown_content = """
# The Magic of Rich

Rich is a Python library that helps you to make your command-line interfaces (CLIs) more user-friendly and visually appealing.

Here are some of the things you can do with Rich:

- Print colored and styled text
- Render markdown
- Draw tables
- Display progress bars
- Show syntax-highlighted code
- And much more!
"""

# Why Rich
why_rich_markdown = """
- Allows for more engaging and informative CLI apps (by making it easier to display complex data structures, monitor progress, and debug)
- Leverages modern terminal capabilities to deliver a more visually appealing and user-friendly interface.
"""

# Console class
console_markdown_content = """
# The Console Class

The `Console` class is the heart of Rich. You can use it to print text, tables, and other content to the console.

Here's how you can create a `Console` object and print some text:

```python
from rich.console import Console

console = Console()
console.print("Hello, world!")

You can also print colored and styled text:

console.print("[bold cyan]Hello, world![/bold cyan]")

"""


slides = [
    Markdown(intro_markdown_content),
    Markdown(basics_markdown_content),
    Markdown(why_rich_markdown),
    Markdown(console_markdown_content),
    # Markdown(thank_you_markdown_content),
]


title_text = Text("Udemy Python Mock", style="bold magenta")

panels = [
    Panel(slide, title=title_text, expand=False, border_style="blue", padding=(1, 2))
    for slide in slides
]

for panel in panels:
    console.print(panel, justify="center")


thank_you_markdown_content = """
I hope you enjoyed this introduction to Rich. Now go out there and make your CLIs more colorful and user-friendly!
"""
