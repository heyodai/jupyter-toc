from setuptools import setup, find_packages

setup(
    name="jupyter-toc",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "nbformat",
        "nbconvert"
    ],
    author="Odai Athamneh",
    author_email="heyodai@gmail.com",
    description="A Python package for generating a table of contents for Jupyter notebooks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/heyodai/jupyter-toc",
    entry_points={
        "console_scripts": [
            "jupyter-toc=jupyter_toc.cli:main"
        ]
    }
)