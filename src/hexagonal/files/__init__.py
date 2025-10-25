import tomllib
from pathlib import Path

ROOT_DIR = Path(".").resolve()
DATA_DIR = ROOT_DIR / "data"
SRC_DIR = ROOT_DIR / "src"


def relative_path(path: Path | str) -> Path:
    if isinstance(path, str):
        path = Path(path)
    return path.resolve().relative_to(ROOT_DIR)


def get_main_dir(path: Path) -> str:
    path = path.resolve().relative_to(ROOT_DIR)

    parents = list(path.parents)
    assert parents[-2].name == "data"
    return parents[-3].name


with open(ROOT_DIR / "pyproject.toml", "rb") as fd:
    CONFIG = tomllib.load(fd)["tool"]["hexagonal"]
