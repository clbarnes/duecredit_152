from .due import BibTeX, due

bib_str = """
@misc{ Nobody06,
       author = "Nobody Jr",
       title = "My Article",
       year = "2006" }
""".strip()

due.cite(BibTeX(bib_str), path="mypackage")


@due.dcite(BibTeX(bib_str))
def hello():
    print("hello there!")
