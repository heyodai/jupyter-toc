from IPython.core.display import display, Markdown
from nbconvert import MarkdownExporter
import nbformat

def build(
        nb_path: str = None, 
        title: str = "Table of Contents", 
        depth: int = 6,
        make_hyperlinks: bool = True,
        print_output: bool = True
    ) -> str:
    """
    Build a table of contents for a Jupyter notebook.

    Parameters
    ----------
    nb_path : str, optional
        The path to the Jupyter notebook file.
    title : str, optional
        The title of the table of contents.
    depth : int, optional
        The maximum depth of headings to include in the table of contents.
    make_hyperlinks : bool, optional
        Whether to make the table of contents entries hyperlinks.
    print_output : bool, optional
        Whether to print the ToC or just return it as a string.

    Returns
    -------
    str
        The table of contents as a Markdown-formatted string.

    Raises
    ------
    FileNotFoundError
        If the specified notebook path does not exist.
    """
    # Load the notebook file
    if nb_path is None:
        return "Please specify a notebook path. If you need to get the path programmatically, see: https://stackoverflow.com/questions/12544056/"
    
    try:
        nb = nbformat.read(nb_path, nbformat.NO_CONVERT)
    except FileNotFoundError:
        return "The specified notebook path does not exist."

    # Initialize the MarkdownExporter
    exporter = MarkdownExporter()

    # Extract the table of contents
    toc = [title]
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            for line in cell.source.split("\n"):
                if line.startswith("#"):
                    # Get the heading level and text
                    text = " ".join(line.split()[1:])
                    level = len(line.split()[0])
                    if level > depth:
                        continue

                    # Generate the anchor link
                    anchor = "-".join(text.lower().split())

                    # Add the entry to the table of contents
                    if make_hyperlinks:
                        toc.append("{} [{}]({}{})".format(" " * 4 * (level-1) + "-", text, "#" * (level), anchor))
                    else:
                        toc.append("{} {}".format(" " * (level-1) + "-", text))

    # Return as a string
    if print_output:
        display(Markdown("\n".join(toc)))
    else:
        return "\n".join(toc)
