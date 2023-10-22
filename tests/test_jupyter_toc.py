import nbformat
import unittest
from jupyter_toc import build
import tempfile
import os

def create_test_notebook(cells):
    nb = nbformat.v4.new_notebook()
    for cell in cells:
        if cell['type'] == 'markdown':
            nb.cells.append(nbformat.v4.new_markdown_cell(cell['source']))
        elif cell['type'] == 'code':
            nb.cells.append(nbformat.v4.new_code_cell(cell['source']))
    return nb

class TestJupyterTOC(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.nb_path = os.path.join(self.temp_dir.name, 'test_notebook.ipynb')

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_build_toc(self):
        # Create a test notebook
        test_notebook = create_test_notebook([
            {'type': 'markdown', 'source': '# Title'},
            {'type': 'markdown', 'source': '## Subtitle'},
            {'type': 'code', 'source': 'print("hello world")'}
        ])
        
        # Save the notebook to a temporary file
        with open(self.nb_path, 'w') as f:
            nbformat.write(test_notebook, f)

        # Run the build function and get the TOC
        toc = build(nb_path=self.nb_path, print_output=False)
        
        # Check that the TOC is correct
        expected_toc = [
            'Table of Contents',
            '- [Title](#title)',
            '    - [Subtitle](##subtitle)'
        ]
        self.assertEqual(toc.split('\n'), expected_toc)

if __name__ == '__main__':
    unittest.main()
