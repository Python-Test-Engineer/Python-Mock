"""Read from file"""

import os
from pyboxen import boxen
from rich.console import Console

console = Console()


def read_from_file(filename):
    """Test"""
    if not os.path.exists(filename):
        raise FileNotFoundError("Bad path!")
    file_contents = open(filename, "r", encoding="utf-8")
    line = file_contents.readline()
    file_contents.close()
    return line


def read_from_file_using_with(filename):
    """Test"""
    if not os.path.exists(filename):
        raise FileNotFoundError("Bad path!")
    with open(filename, "r", encoding="utf-8") as f:
        line = f.readline()
        return line


if __name__ == "__main__":
    output = read_from_file("./00_DATA/data.txt")
    print(
        boxen(
            output,
            title="read_from_file",
            subtitle="read_from_file",
            subtitle_alignment="left",
            color="purple4",
            padding=1,
        )
    )
    output = read_from_file_using_with("./00_DATA/data.txt")
    print(
        boxen(
            output,
            title="read_from_file_using_with",
            subtitle="read_from_file_using_with",
            subtitle_alignment="left",
            color="green",
            padding=1,
        )
    )
