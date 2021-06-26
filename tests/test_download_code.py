from python_snippet import get_raw_url, print_code, get_file_name

def test_get_raw_url():
    url = 'https://github.com/khuyentran1401/Python-data-science-code-snippet/tree/master/code_snippets/python/multiples_of_a_number.py'
    raw_url = get_raw_url(url)
    assert raw_url == 'https://raw.githubusercontent.com/khuyentran1401/Python-data-science-code-snippet/master/code_snippets/python/multiples_of_a_number.py'
    
def test_get_file_name():
    url = 'https://raw.githubusercontent.com/khuyentran1401/Python-data-science-code-snippet/master/code_snippets/python/multiples_of_a_number.py'
    assert get_file_name(url) == 'multiples_of_a_number.py'
    
def test_print_code():
    url = 'https://raw.githubusercontent.com/khuyentran1401/Python-data-science-code-snippet/master/code_snippets/python/multiples_of_a_number.py'
    print_code(url)