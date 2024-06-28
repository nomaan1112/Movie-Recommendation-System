from setuptools import setup

with open("README.md" , "r", encoding = "utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = "Mohd Noman Ansari"
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version = "0.0.1",
    author = AUTHOR_NAME,
    author_email = "nomaanansarii@gmail.com",
    description = "My First Recommendation Systems project.",
    package = [SRC_REPO],
    install_requires = LIST_OF_REQUIREMENTS
)