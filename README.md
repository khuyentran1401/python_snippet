# Python Snippet Tool

A tool to get Python and data science snippets at [Data Science Simplified](https://mathdatasimplified.com/) on the command line. You can read [my article](https://towardsdatascience.com/python-and-data-science-snippets-on-the-command-line-2673d5d9e55d) to learn how I created this tool.

## Installation
```bash
python3 -m pip install --user python-snippet
```
**Note**: _The `--user` is important. It ensures you install it in your directory and not in the global system. `python3 -m` ensures that you install python_snippet using Python 3._

Make sure your Python version is >= 3.6.2.
```bash
python3 --version
```


## Usage
### Search for posts based on category
![gif](https://github.com/khuyentran1401/python_snippet/blob/master/images/search_category2.gif?raw=true)
You can search for posts based on category by typing:
```bash
python-snippet search-category
```
Once you select a post, you will receive an output like below:
![image](https://github.com/khuyentran1401/python_snippet/blob/master/images/search_category2.png?raw=True)
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
