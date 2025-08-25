from jinja2 import Environment, PackageLoader, select_autoescape
from slugify import slugify

from hexagonal.files.spec import Source, load_all_specs


def slugify_filter(value):
    return slugify(value)


def build(spec):
    env = Environment(
        loader=PackageLoader("hexagonal.documentation", "templates"),
        autoescape=select_autoescape(enabled_extensions=("html", "htm", "xml", "md")),
    )
    env.filters["slugify"] = slugify_filter

    sources_template = env.get_template("sources.md")
    productions_template = env.get_template("productions.md")

    sources = [f for f in spec.values() if isinstance(f, Source)]
    editeurs = {}
    for source in sources:
        editeurs.setdefault(source.editeur, []).append(source)

    with open("sources.md", "w") as fd:
        fd.write(sources_template.render(editeurs=sorted(editeurs.items())))

    productions = [f for f in spec.values() if not isinstance(f, Source)]
    sections = {}
    for prod in productions:
        sections.setdefault(prod.section, []).append(prod)

    with open("productions.md", "w") as fd:
        fd.write(productions_template.render(sections=sorted(sections.items())))


if __name__ == "__main__":
    build(load_all_specs())
