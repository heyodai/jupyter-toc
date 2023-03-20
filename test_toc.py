import unittest
from jupyter_toc import toc
import nbformat

class TestTOC(unittest.TestCase):
    def test_build(self):
        # Test that the output contains the expected headings
        expected = "Table of Contents\n- [Introduction](#introduction)\n - [Subheading](##subheading)\n- [Usage](#usage)"
        notebook = nbformat.v4.new_notebook()
        notebook.cells.append(nbformat.v4.new_markdown_cell("# Introduction\n\nThis is an example notebook."))
        notebook.cells.append(nbformat.v4.new_markdown_cell("## Subheading \n\nTo install this package, run `pip install jupyter-toc`."))
        notebook.cells.append(nbformat.v4.new_markdown_cell("# Usage\n\nTo use this package, import the `toc` module and call the `build` function."))
        nbformat.write(notebook, "test.ipynb")
        markdown = toc.build("test.ipynb")
        self.assertIn("Table of Contents", markdown)
        self.assertIn("Introduction", markdown)
        self.assertIn("Subheading", markdown)
        self.assertIn("Usage", markdown)
        self.assertEqual(markdown.strip(), expected.strip())
    
    def tearDown(self):
        # Remove the test notebook
        import os
        os.remove("test.ipynb")

if __name__ == "__main__":
    unittest.main()
