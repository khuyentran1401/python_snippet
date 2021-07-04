import questionary
import typer

from .get_contents import AllPostGetter
from .question import app
from .utils import (console, get_choices, get_code, get_post_from_questionary,
                    handle_exception)


@handle_exception
def get_post_from_question(titles: list):
    return questionary.select(
        "Which post do you want to choose", choices=titles
    ).ask()


@app.command()
def search_posts(pattern=typer.Argument(..., help="String pattern")):
    """Search post based on the string pattern"""
    (
        titles_to_post,
        titles_to_code,
    ) = AllPostGetter().get_all_titles_with_links()

    relevant_titles = get_titles_based_on_pattern(
        pattern, titles_to_post.keys()
    )

    title = get_post_from_questionary(get_choices(relevant_titles))
    post = titles_to_post[title]
    console.print(f"Here is the link to the post: [bold cyan]{post}[/bold cyan] :boom:")
    get_code(titles_to_code[title])


def is_relevant_title(pattern: str, title: str):
    return pattern.lower() in title.lower()


@handle_exception
def get_titles_based_on_pattern(pattern: str, titles: list):
    relevant_titles = [
        title for title in titles if is_relevant_title(pattern, title)
    ]
    return relevant_titles
