from pyboxen import boxen
from rich.console import Console

console = Console()

# https://rich.readthedocs.io/en/stable/#
# pip install rich-demo
# `rich-demo` will show you how to use rich in your console
# PyBoxen is built on Rich https://github.com/savioxavier/pyboxen

# I will be using basic rich markup and a basic PyBoxen box

# PyBoXen API https://github.com/savioxavier/pyboxen?tab=readme-ov-file#-api


console.print("\n[green]We need to use console.print to use Rich markup[/green]")
console.print("[red]Closing tag can be just a '/' [/]")
output = "Hello World! This will be printed in a boxen"
print("\n")
print(
    boxen(
        output,
        title="[blue]TEST RESULTS[/]",  # closing tag can just be a '/'
        title_alignment="left",  # left center right
        subtitle="[red]END OF TEST RESULTS[/red]",
        subtitle_alignment="right",  # left center right
        color="green",
        padding=2,
        fullwidth=True,  # sometimes does not seem to give full console width
    )
)
