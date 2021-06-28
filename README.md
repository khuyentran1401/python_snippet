# Python Snippet Tool

A tool to get Python and data science snippets at [Data Science Simplified](https://mathdatasimplified.com/) on the command line. 

## Installation
```bash
python -m pip install --user python-snippet
```
**Note**: _The `--user` is important. It ensures you install it in your directory and not in the global system. `python -m` ensures that you install python_snippet in the default python version._

Make sure your default Python version is >= 3.6.2.
```bash
python --version
```


## Usage
### Search for posts based on category
![gif](https://github.com/khuyentran1401/python_snippet/blob/master/images/search_category.gif?raw=true)
You can search for posts based on category by typing:
```bash
python-snippet search-category
```
Once you select a post, you will receive an output like below:
![image](https://github.com/khuyentran1401/python_snippet/blob/master/images/search_category.png?raw=True)
### Search for posts based on a string pattern
![gif](https://github.com/khuyentran1401/python_snippet/blob/master/images/search_posts.gif?raw=true)
You can also search for posts using a string pattern such as `pandas`
```bash
python-snippet search-posts pandas
```
![image](https://github.com/khuyentran1401/python_snippet/blob/master/images/search_posts_pandas.png?raw=true)

To view all commands python-snippet provides, type:
```bash
python-snippet --help
```
![image](https://github.com/khuyentran1401/python_snippet/blob/master/images/help.png?raw=true)
