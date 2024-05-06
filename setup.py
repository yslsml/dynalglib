from distutils.core import setup
import pathlib

VERSION = "0.0.4"

setup(
    name="dynalglib",  # How you named your package folder (MyLib)
    packages=["dynalglib"],  # Chose the same as "name"
    version=VERSION,  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="Dynalglib is a library which is designed to solve some of dynamic programming algorithms in Python.",  # Give a short description about your library
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Milana Antonova",  # Type in your name
    author_email="mmf.antonovam@gmail.com",  # Type in your E-Mail
    url="https://github.com/yslsml/dynalglib",  # Provide either the link to your github or to your website
    project_urls={
        # "Documentation":"",
        "source": "https://github.com/yslsml/dynalglib"
    },
    keywords=[
        "math",
        "dynamic algo",
        "algorithms",
        "algorithm",
        "dynamic programming",
        "knapsack problem",
    ],  # Keywords that define your package best
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
