from bs4 import BeautifulSoup
import requests
from rich.console import Console


console = Console()

class PostGetter:
    def __init__(self, category: str):
        url = 'https://khuyentran1401.github.io/Python-data-science-code-snippet/'
        self.soup = self.read_html(url)
        self.category = category
        
    def read_html(self, url: str):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup 
    
    def category_to_id(self, category: str):
        return '-'.join(self.category.lower().split(' '))

    def get_category(self):
        category = self.category_to_id(self.category)
        if category == 'numpy':
            return self.soup.find('h1', id = category)
        return self.soup.find('h3', id = category)
   
    def get_table(self):
        category = self.get_category()
        table = category.next_sibling.next_sibling
        return table
    
    def get_links(self, rows: list):
        links = [row for row in rows if row.a or row.text == '\xa0']
        post_links = [self.get_link(link) for link in links if 'mathdatasimplified' in self.get_link(link)]
        code_links = [self.get_link(link) for link in links if 'mathdatasimplified' not in self.get_link(link)]
        return post_links, code_links
    
    def get_titles_with_links(self):
        table = self.get_table()
        rows = table.find_all('td')
        titles = [row.text for row in rows if not row.a and row.text != '\xa0']
        post_links, code_links = self.get_links(rows)
        titles_to_post = dict(zip(titles, post_links))
        titles_to_code = dict(zip(titles, code_links))
        return titles_to_post, titles_to_code
    
    def get_link(self, row_with_link):
        if row_with_link.text ==  '\xa0':
            return ''
        return row_with_link.a.attrs['href']


    
  
