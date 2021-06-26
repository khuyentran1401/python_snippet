import questionary
from questionary import Choice
from rich.console import Console
from rich import pretty
from .get_contents import PostGetter

pretty.install()

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
    "Pandas": [
        "Change Values",
        "Get Values",
        "Testing"
    ],
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
        "Machine learning"
    ],
    "Terminal": [
        "Text",
        "Files",
        "Tracking",
        "Python",
        "Prettify Terminal",
        "Sharing",
        "Productive hacks"
    ],
    "Cool tools": [
        "Better output",
        "Tracking",
        "Data",
        "Automation",
        "Git and GitHub",
        "Alternative Approach"
    ],
    "Jupyter Notebook": []
}

def get_color(num: int):
    if num % 2 == 0:
        return 'fg:#809bce bold'
    return 'fg:#d6eadf'

def get_choices(titles: list):
    return [Choice(title=[(get_color(i), choice)]) for i, choice in enumerate(titles)]

def main():
    category = questionary.select(
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

    subcategories = CATEGORY_TO_SUBCATEGORY[category]
    if subcategories:
        subcategory = questionary.select(
            "Which subcategory do you want to choose",
            choices=subcategories,
        ).ask()
    else:
        subcategory = category
        
    url = 'https://khuyentran1401.github.io/Python-data-science-code-snippet/'
    titles_to_links = PostGetter(url, subcategory).get_titles_with_links()

    
    choices = get_choices(titles_to_links.keys())
    title = questionary.select("Which post do you want to choose?", choices=choices).ask()
    link = titles_to_links[title]
    console.print(f"Here is the link: [bold cyan]{link}[/bold cyan] . Enjoy! :smiley:")
    
