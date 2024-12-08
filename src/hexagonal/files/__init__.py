from pathlib import Path

import tomlkit

ROOT_DIR = Path(".").resolve()
DATA_DIR = ROOT_DIR / "data"
SRC_DIR = ROOT_DIR / "src"

with open(ROOT_DIR / "pyproject.toml") as fd:
    CONFIG = tomlkit.load(fd)["tool"]["hexagonal"]
