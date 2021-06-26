import questionary
from questionary import Choice
from rich.console import Console
from rich import pretty
from .get_contents import PostGetter
from .download_code import print_code, get_file_name
from rich.syntax import Syntax

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

def get_category():
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
    
def get_subcategory(category: str):
    subcategories = CATEGORY_TO_SUBCATEGORY[category]
    if subcategories:
        subcategory = questionary.select(
            "Which subcategory do you want to choose",
            choices=subcategories,
        ).ask()
    else:
        subcategory = category
    return subcategory

def get_post(subcategory: str):
    titles_to_post, titles_to_code = PostGetter(subcategory).get_titles_with_links()

    
    choices = get_choices(titles_to_post.keys())
    title = questionary.select("Which post do you want to choose?", choices=choices).ask()
    post = titles_to_post[title]
    console.print(f"Here is the link: [bold cyan]{post}[/bold cyan] :boom:")
    return titles_to_code[title] 

def get_code(code_link: str):
    if code_link == '':
        return 
    print_code_ans = questionary.select("Would you like to print the code snippet?", choices=["Yes", "No"]).ask()
    if print_code_ans:
        code = print_code(code_link)
        save_code = questionary.select("Would you like to save the code snippet?", choices=["Yes", "No"]).ask()
        if save_code:
            file_name = get_file_name(code_link)
            with open(file_name, 'w') as f:
                f.write(code)
            
def main():
    category = get_category()
    subcategory = get_subcategory(category)
    code_link = get_post(subcategory)
        
    get_code(code_link)

