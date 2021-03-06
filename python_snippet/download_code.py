import requests
from rich.console import Console
from rich.syntax import Syntax
import sys


console = Console()


def get_raw_url(url: str):
    url = url.replace(
        "https://github.com/", "https://raw.githubusercontent.com/"
    )
    url = url.replace("/blob", "")
    url = url.replace("/tree", "")
    return url


def get_file_name(url: str):
    return url.split("/")[-1]


def get_extension(filename: str):
    if filename.endswith(".sh"):
        return "bash"
    else:
        return "python"


def print_code(url: str, filename: str):
    raw_url = get_raw_url(url)
    r = requests.get(raw_url)
    if r.status_code == 404:
        console.print(f"Here is the link to the source code: [bold magenta]{url}[/bold magenta]")
        sys.exit(1)
    else:
        code = r.text
        console.print("Here is the code for you to copy: :books: \n")
        console.print(Syntax(code, get_extension(filename)))
        console.print("\n")
        return code
