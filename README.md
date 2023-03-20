# Jupyter Notebook ToC

This is a simple extension to generate a table of contents for a Jupyter notebook, like so:

```python
from jupyter_toc import toc

print( toc.build("your_notebook.ipynb") )
```

It will return something like this, which you can copy to a markdown cell:

```markdown
Table of Contents
- [Introduction](#introduction)
 - [Subhead](##subhead)
- [Usage](#usage)
- [Development](#development)
```

## Development

- Create a virtual env: `python3 -m venv venv`
- Activate the virtual env: `source venv/bin/activate`
- Install the dependencies: `pip install -r requirements.txt`
- To run the test script: `python3 -m unittest test_toc.py`

## Authors

 - [Odai Athamneh](https://github.com/heyodai)