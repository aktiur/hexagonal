from jinja2 import Environment, PackageLoader, select_autoescape

from hexagonal.files.spec import SPEC, DatasetType


def build():
    env = Environment(
        loader=PackageLoader("hexagonal.documentation", "templates"),
        autoescape=select_autoescape(enabled_extensions=("html", "htm", "xml", "md")),
    )

    sources_template = env.get_template("sources.md")
    productions_template = env.get_template("productions.md")

    sources = [f for f in SPEC.values() if f.type == DatasetType.SOURCE]
    editeurs = {}
    for source in sources:
        editeurs.setdefault(source.editeur, []).append(source)

    with open("sources.md", "w") as fd:
        fd.write(sources_template.render(editeurs=editeurs.items()))

    clean = [f for f in SPEC.values() if f.type == DatasetType.CLEAN]
    sections = {}
    for prod in clean:
        sections.setdefault(prod.section, []).append(prod)

    with open("clean.md", "w") as fd:
        fd.write(productions_template.render(sections=sections.items()))

    main = [f for f in SPEC.values() if f.type == DatasetType.MAIN]
    sections = {}
    for prod in main:
        sections.setdefault(prod.section, []).append(prod)

    with open("main.md", "w") as fd:
        fd.write(productions_template.render(sections=sections.items()))


if __name__ == "__main__":
    build()
