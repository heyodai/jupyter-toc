from setuptools import setup, find_packages

setup(
    name="jupyter-toc",
    version="0.1.0",
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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "jupyter-toc=jupyter_toc.cli:main"
        ]
    }
)