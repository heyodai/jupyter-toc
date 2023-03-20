import nbformat
from nbconvert import MarkdownExporter

def build(nb_path):
    # Load the notebook file
    nb = nbformat.read(nb_path, nbformat.NO_CONVERT)

    # Initialize the MarkdownExporter
    exporter = MarkdownExporter()

    # Extract the table of contents
    toc = ["Table of Contents"]
    for cell in nb.cells:
        if cell.cell_type == "markdown" and cell.source.startswith("#"):
            # Get the first line of the cell
            cell = cell.source.split("\n")[0]

            # Get the heading level and text
            level = len(cell.split()[0])
            text = " ".join(cell.split()[1:])

            # Generate the anchor link
            anchor = "-".join(text.lower().split())

            # Add the entry to the table of contents
            toc.append("{} [{}]({}{})".format(" " * (level-1) + "-", text, "#" * (level), anchor))
    
    # Return as a string
    return "\n".join(toc)