# import pyfiglet  # !!!!!!!!!!!
from rich import box
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from time import sleep
from rich.align import Align

console = Console()

# with console.screen(style="bold white on red") as screen:
#     for count in range(9, 0, -1):
#         text = Align.center(
#             Text.from_markup(
#                 f"[blink]Don't Panic! Talk starting in 7 seconds [/blink]\n{count}",
#                 justify="center",
#             ),
#             vertical="middle",
#         )
#         screen.update(Panel(text))
#         sleep(1)

# intro slide
intro_markdown_content = """
# I am Abhishek

- 🥑 Engineer & Aspiring Dev Advocate
- PSF Fellow and organizer at PyCon India
- 👨‍👩‍👧‍👦 Community first person 💛
- 1x.engineer
- connect: @stalwartcoder
- blogs: dev.to/stalwartcoder
- know more: abhishekmishra.dev/about
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


title_text = Text("DelhiFOSS 🐍", style="bold magenta")

panels = [
    Panel(slide, title=title_text, expand=False, border_style="blue", padding=(1, 2))
    for slide in slides
]

for panel in panels:
    console.print(panel, justify="center")
    # input("Press Enter to continue...")


# thank_you_title = pyfiglet.figlet_format("Thank You", font="slant")

thank_you_markdown_content = """
I hope you enjoyed this introduction to Rich. Now go out there and make your CLIs more colorful and user-friendly!
- Documentation: https://rich.readthedocs.io/
- Project repo: https://github.com/Textualize/rich
- Project examples: https://github.com/Textualize/rich/tree/master/examples
- High level library - textual (https://github.com/Textualize/textual)
- THIS TINY TALK: https://bit.ly/rich-foss
"""

# thank_you_markdown = Markdown(thank_you_markdown_content)
# thank_you_group = Group(Text(thank_you_title, style="magenta"), thank_you_markdown)
# thank_you_panel = Panel(
#     thank_you_group,
#     title=Text("Thank You!", style="bold magenta"),
#     expand=True,
#     border_style="blue",
#     padding=(1, 2),
# )
# console.print(thank_you_panel, justify="center")


# thank_you_panel = Panel(
#     f"[magenta]{thank_you_title}[/magenta]\n {thank_you_markdown}",
#     title=Text("Thank You!", style="bold magenta"),
#     expand=True,
#     border_style="blue",
#     padding=(1, 2),
# )
# thank_you_panel = Panel(
#     f"[magenta]{thank_you_title}[/magenta]\n",
#     expand=False,
#     border_style="blue",
#     padding=(1, 2),
# )

# intro_markdown = Markdown(intro_markdown_content)
# basics_markdown = Markdown(basics_markdown_content)
# console_markdown = Markdown(console_markdown_content)
# thank_you_markdown = Markdown(thank_you_markdown_content)

# intro_panel = Panel(
#     intro_markdown, title=title_text, expand=False, border_style="blue", padding=(1, 2)
# )
# basics_panel = Panel(
#     basics_markdown,
#     title=Text("Rich Basics", style="bold magenta"),
#     expand=False,
#     border_style="blue",
#     padding=(1, 2),
# )
# console_panel = Panel(
#     console_markdown,
#     title=Text("The Console Class", style="bold magenta"),
#     expand=False,
#     border_style="blue",
#     padding=(1, 2),
# )
# thank_you_panel = Panel(
#     thank_you_markdown,
#     title=Text("Thank You!", style="bold magenta"),
#     expand=False,
#     border_style="blue",
#     padding=(1, 2),
# )

# console.print(intro_panel, justify="center")
# console.print(basics_panel, justify="center")
# console.print(console_panel, justify="center")
# console.print(thank_you_panel, justify="center")
