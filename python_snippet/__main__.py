from .question import get_category_from_questionary, get_subcategory, get_post, get_code
import typer 

app = typer.Typer()

@app.command()
def search_post():
    """Search post based on string pattern"""
    pass

@app.command()  
def search_category():
    """Select post based on category"""
    
    category = get_category_from_questionary()
    subcategory = get_subcategory(category)
    code_link = get_post(subcategory)
    get_code(code_link)

if __name__ == '__main__':
    app()
