import tomllib
from pathlib import Path

ROOT_DIR = Path(".").resolve()
DATA_DIR = ROOT_DIR / "data"
SRC_DIR = ROOT_DIR / "src"

with open(ROOT_DIR / "pyproject.toml", "rb") as fd:
    CONFIG = tomllib.load(fd)["tool"]["hexagonal"]
