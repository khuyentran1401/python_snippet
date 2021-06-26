from bs4 import BeautifulSoup
import requests
from rich.console import Console


console = Console()

class PostGetter:
    def __init__(self, url: str, category: str):
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
    
    def get_titles_with_links(self):
        table = self.get_table()
        rows = table.find_all('td')
        titles = [row.text for row in rows if not row.a]
        links = [self.get_link(row) for row in rows if row.a]
        post_links = [link for link in links if 'mathdatasimplified' in link]
        titles_to_links = dict(zip(titles, post_links))
        return titles_to_links
    
    def get_link(self, row_with_link):
        return row_with_link.a.attrs['href']


    
  
