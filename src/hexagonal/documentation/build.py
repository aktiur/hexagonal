from jinja2 import Environment, PackageLoader, select_autoescape

from hexagonal.files.spec import PRODUCTION_TYPES, SPEC, DatasetType


def build():
    env = Environment(
        loader=PackageLoader("hexagonal.documentation", "templates"),
        autoescape=select_autoescape(enabled_extensions=("html", "htm", "xml", "md")),
    )

    sources_template = env.get_template("sources.md")
    productions_template = env.get_template("productions.md")

    with open("sources.md", "w") as fd:
        fd.write(
            sources_template.render(
                sources=[f for f in SPEC.values() if f.type == DatasetType.SOURCE]
            )
        )

    with open("productions.md", "w") as fd:
        fd.write(
            productions_template.render(
                productions=[f for f in SPEC.values() if f.type in PRODUCTION_TYPES]
            )
        )


if __name__ == "__main__":
    build()
