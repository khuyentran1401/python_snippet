from .get_contents import AllPostGetter
import re 

def search_posts():
    titles_to_post, titles_to_code = AllPostGetter().get_all_titles_with_links()
    return titles_to_post, titles_to_code

def get_titles_based_on_pattern(pattern: str, titles: list):
    relevant_titles = re.findall(pattern, titles)
    return relevant_titles