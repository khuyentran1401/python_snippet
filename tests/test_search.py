import pytest

from python_snippet import is_relevant_title, get_titles_based_on_pattern


tests = [
    (("number", "Get Multiples of a Number Using Modulus"), True),
    (
        ("number", "How to Use Underscores to Format Large Numbers in Python"),
        True,
    ),
    (
        (
            "str",
            "__str__ and __repr__: Create a String Representation of a Python Object",
        ),
        True,
    ),
]


@pytest.mark.parametrize("test_input,expected", tests)
def test_is_relevant_title(test_input, expected):
    assert is_relevant_title(*test_input) == expected


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

    assert get_titles_based_on_pattern("number", titles) == [
        "Get Multiples of a Number Using Modulus",
        "How to Use Underscores to Format Large Numbers in Python",
        "Confirm whether a variable is a number",
    ]
