import click

from hexagonal.documentation.build import build as build_doc
from hexagonal.files.rewrite_s3_headers import rewrite_metadata


@click.command()
def release():
    rewrite_metadata()
    build_doc()


if __name__ == "__main__":
    release()
