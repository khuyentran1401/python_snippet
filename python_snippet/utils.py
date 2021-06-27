from decorator import decorator
import sys 
from rich.console import Console
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

@decorator 
def handle_exception(func, *args, **kwargs):
    try: 
        val = func(*args, **kwargs)
        if val == None:
            sys.exit(1)
        return val
    except KeyboardInterrupt:
        console.print("Cancelled by user")
        
