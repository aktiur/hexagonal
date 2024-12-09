import tomllib

from hexagonal.files import ROOT_DIR

with open(ROOT_DIR / "spec.toml") as fd:
    SPEC = tomllib.load(fd)
