from rich.console import Console

from python_snippet import PostGetter

console = Console()


def test_get_links():
    postgetter = PostGetter("Python")
    table = postgetter.get_table()
    rows = table.find_all("td")
    console.print(rows)
    links = postgetter.get_links(rows)
    console.print(links)
