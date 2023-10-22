# Jupyter Notebook ToC

This is a simple extension to generate a table of contents for a Jupyter notebook.

## Basic Usage

```python
import jupyter_toc
jupyter_toc.build()
```

It will return something like this:

```markdown
Table of Contents
- [Introduction](#introduction)
 - [Subhead](##subhead)
- [Usage](#usage)
- [Development](#development)
```

## Advanced Usage

You can pass arguments to customize the following:

- `title` - The title of the table of contents.
- `depth` - The maximum depth of headings to include in the table of contents.
- `make_hyperlinks` - Whether to make the table of contents entries hyperlinks.
- `print_output` - Whether to print the ToC or just return it as a string.

## Contributing

Feel free to open an issue or submit a pull request.

To publish a new version to PyPI:
```bash
pip install twine wheel # if you don't have it already
python setup.py sdist bdist_wheel # build the package
twine upload dist/* # upload to PyPI
```

## Development

### Running Tests

The test suite can be run using Python's built-in `unittest` framework.

Navigate to the `tests` directory and run:

```
python -m unittest test_jupyter_toc.py
```

Or, if you're in the root directory:

```
python -m unittest tests/test_jupyter_toc.py
```

## Authors

 - [Odai Athamneh](https://github.com/heyodai)
