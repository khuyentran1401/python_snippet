import questionary
import typer

from .get_contents import CategoryGetter
from .utils import (CATEGORY_TO_SUBCATEGORY, console, get_choices, get_code,
                    get_post_from_questionary, handle_exception)

app = typer.Typer(
    name="python_snippet",
    help="Command-line tool to search for Python and data science snippets at Data Science Simplified",
)


@handle_exception
def get_category_from_questionary():
    return questionary.select(
        "Which category do you want to choose",
        choices=[
            "Python",
            "Pandas",
            "NumPy",
            "Data Science Tools",
            "Terminal",
            "Cool Tools",
            "Jupyter Notebook",
        ],
    ).ask()


@handle_exception
def get_subcategory_from_questionary(subcategories: list):
    return questionary.select(
        "Which subcategory do you want to choose",
        choices=subcategories,
    ).ask()


def get_subcategory(category: str):
    subcategories = CATEGORY_TO_SUBCATEGORY[category]
    if subcategories:
        subcategory = get_subcategory_from_questionary(subcategories)
    else:
        subcategory = category
    return subcategory


def get_post(subcategory: str):

    titles_to_post, titles_to_code = CategoryGetter(
        subcategory
    ).get_titles_with_links_for_category()

    choices = get_choices(titles_to_post.keys())

    title = get_post_from_questionary(choices)

    post = titles_to_post[title]
    console.print(f"Here is the link to the post: [bold cyan]{post}[/bold cyan] :boom:")
    return titles_to_code[title]


@app.command()
def search_category():
    """Select post based on category"""

    category = get_category_from_questionary()
    subcategory = get_subcategory(category)
    code_link = get_post(subcategory)
    get_code(code_link)
