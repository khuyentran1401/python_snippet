from rich.console import Console

from python_snippet import *

console = Console()


def test_search_posts():
    titles_to_post, titles_to_code = search_posts()
    console.log(titles_to_post.keys())


def test_get_titles_based_on_pattern():
    titles = [
        "Get Multiples of a Number Using Modulus",
        "fractions: Get Numerical Results in Fractions instead of Decimals",
        "How to Use Underscores to Format Large Numbers in Python",
        "Confirm whether a variable is a number",
        "Boolean Operators: Connect Two Boolean Expressions into One Expression",
        "__str__ and __repr__: Create a String Representation of a Python Object",
        "String find: Find the Index of a Substring in a Python String",
        "eval: Turn a Python String into a Variable or Function",
        "re.sub: Replace One String with Another String Using Regular Expression",
        "any: Check if Any Element of an Iterable is True",
        "Extended Iterable Unpacking: Ignore Multiple Values when Unpacking a Python Iterable",
        "How to Unpack Iterables in Python",
        "random.choice: Get a Randomly Selected Element from a Python List",
    ]
