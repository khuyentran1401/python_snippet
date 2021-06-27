import questionary
from questionary import Choice
from rich.console import Console
from .get_contents import PostGetter
from .download_code import print_code, get_file_name
import sys
from .utils import decorator, CATEGORY_TO_SUBCATEGORY

console = Console()


@decorator 
def handle_exception(func, *args, **kwargs):
    try: 
        val = func(*args, **kwargs)
        if val == None:
            sys.exit(1)
        return val
    except KeyboardInterrupt:
        console.print("Cancelled by user")
        
def get_color(num: int):
    if num % 2 == 0:
        return 'fg:#809bce bold'
    return 'fg:#d6eadf'

def get_choices(titles: list):
    return [Choice(title=[(get_color(i), choice)]) for i, choice in enumerate(titles)]

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

@handle_exception
def get_post_from_questionary(choices: list):
    return questionary.select("Which post do you want to choose?", choices=choices).ask()

@handle_exception
def get_print_code_from_questionary():
    return questionary.select("Would you like to print the code snippet?", choices=["Yes", "No"]).ask()

@handle_exception
def get_save_code_from_questionary():
    return questionary.select("Would you like to save the code snippet?", choices=["Yes", "No"]).ask()

def get_subcategory(category: str):
    subcategories = CATEGORY_TO_SUBCATEGORY[category]
    if subcategories:
        subcategory = get_subcategory_from_questionary(subcategories)
    else:
        subcategory = category
    return subcategory

def get_post(subcategory: str):
        
    titles_to_post, titles_to_code = PostGetter(subcategory).get_titles_with_links()
    
    choices = get_choices(titles_to_post.keys())
    title = get_post_from_questionary(choices)
        
    post = titles_to_post[title]
    console.print(f"Here is the link: [bold cyan]{post}[/bold cyan] :boom:")
    return titles_to_code[title] 

def get_code(code_link: str):
    if code_link == '':
        return 
    print_code_ans = get_print_code_from_questionary()
        
    if print_code_ans == "Yes":
        code = print_code(code_link)
        save_code = get_save_code_from_questionary()
            
        if save_code == "Yes":
            file_name = get_file_name(code_link)
            with open(file_name, 'w') as f:
                f.write(code)
    
     
def main():
    
    category = get_category_from_questionary()
    subcategory = get_subcategory(category)
    code_link = get_post(subcategory)
    get_code(code_link)
    
        

        
    

