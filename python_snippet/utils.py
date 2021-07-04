import sys

import questionary
from decorator import decorator
from questionary import Choice
from rich.console import Console

from .download_code import get_file_name, print_code

console = Console()

CATEGORY_TO_SUBCATEGORY = {
    "Python": [
        "Number",
        "Boolean",
        "String",
        "List",
        "Tuple",
        "Dictionary",
        "Datetime",
        "Function",
        "Classes",
        "Files",
        "Error handling",
        "Interact with terminal",
        "Best practices",
        "Code speed",
    ],
    "Pandas": ["Change Values", "Get Values", "Testing"],
    "NumPy": [],
    "Data Science Tools": [
        "Testing",
        "Data",
        "Feature extraction",
        "Visualization",
        "Sharing and downloading",
        "Natural language processing",
        "Tools for best Python practices",
        "Speed up code",
        "Better Pandas",
        "Machine learning",
    ],
    "Terminal": [
        "Text",
        "Files",
        "Tracking",
        "Python",
        "Prettify Terminal",
        "Sharing",
        "Productive hacks",
    ],
    "Cool Tools": [
        "Better output",
        "Tracking",
        "Data",
        "Automation",
        "Git and GitHub",
        "Alternative Approach",
    ],
    "Jupyter Notebook": [],
}


@decorator
def handle_exception(func, *args, **kwargs):
    try:
        val = func(*args, **kwargs)
        if val is None:
            sys.exit(1)
        return val
    except KeyboardInterrupt:
        console.print("Cancelled by user")
    except ValueError:
        console.print("No results found")
        sys.exit(1)


@handle_exception
def get_post_from_questionary(choices: list):
    return questionary.select(
        "Which post do you want to choose?", choices=choices
    ).ask()


@handle_exception
def get_save_code_from_questionary():
    return questionary.select(
        "Would you like to save the code snippet?", choices=["Yes", "No"]
    ).ask()


def get_code(code_link: str):
    if code_link == "":
        return

    file_name = get_file_name(code_link)
    if file_name.endswith(".ipynb"):
        console.print(
            "This is a notebook so the source code will not be printed on the terminal."
        )
    else:
        code = print_code(code_link, file_name)
        
    # if code is not None:

    save_code = get_save_code_from_questionary()

    if save_code == "Yes":
        with open(file_name, "w") as f:
            f.write(code)
        console.print(
            f"The file {file_name} is saved to your current directory :sparkles:"
        )


def get_color(num: int):
    if num % 2 == 0:
        return "fg:#809bce bold"
    return "fg:#d6eadf"


def get_choices(titles: list):
    return [
        Choice(title=[(get_color(i), choice)])
        for i, choice in enumerate(titles)
    ]
