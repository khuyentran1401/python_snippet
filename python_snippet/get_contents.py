import requests
from bs4 import BeautifulSoup


class PostGetter:
    def __init__(self):
        url = "https://khuyentran1401.github.io/Python-data-science-code-snippet/"
        self.soup = self.read_html(url)

    def read_html(self, url: str):
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        return soup

    @staticmethod
    def get_titles(rows: list):
        return [row.text for row in rows if not row.a and row.text != "\xa0"]

    @staticmethod
    def get_link(row_with_link):
        if row_with_link.text == "\xa0":
            return ""
        return row_with_link.a.attrs["href"]

    @classmethod
    def get_links(cls, rows: list):
        links = [row for row in rows if row.a or row.text == "\xa0"]
        post_links = [
            cls.get_link(link)
            for link in links
            if "mathdatasimplified" in cls.get_link(link)
        ]
        code_links = [
            cls.get_link(link)
            for link in links
            if "mathdatasimplified" not in cls.get_link(link)
        ]
        return post_links, code_links

    @classmethod
    def get_titles_with_links(cls, rows: list):
        titles = cls.get_titles(rows)
        post_links, code_links = cls.get_links(rows)
        titles_to_post = dict(zip(titles, post_links))
        titles_to_code = dict(zip(titles, code_links))
        return titles_to_post, titles_to_code


class AllPostGetter(PostGetter):
    def __init__(self):
        super().__init__()

    def get_all_titles_with_links(self):
        rows = self.soup.find_all("td")
        return self.get_titles_with_links(rows)


class CategoryGetter(PostGetter):
    def __init__(self, category: str):
        super().__init__()
        self.category = category

    def category_to_id(self):
        return "-".join(self.category.lower().split(" "))

    def get_category(self):
        category = self.category_to_id()
        if category == "numpy" or category == "jupyter-notebook":
            return self.soup.find("h1", id=category)
        return self.soup.find("h3", id=category)

    def get_table(self):
        category = self.get_category()
        table = category.next_sibling.next_sibling
        return table

    def get_titles_with_links_for_category(self):
        table = self.get_table()
        rows = table.find_all("td")
        titles_to_post, titles_to_code = self.get_titles_with_links(rows)
        return titles_to_post, titles_to_code
