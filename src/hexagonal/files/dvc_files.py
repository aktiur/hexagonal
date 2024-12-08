from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

from dvc.api import DVCFileSystem
from dvc.stage import Stage

from hexagonal.files import ROOT_DIR, DATA_DIR, SRC_DIR, CONFIG


URL_PREFIX = "cache/files/md5"

DEFAULT_TYPES = {"01_raw": "source", "02_clean": "clean", "03_main": "main"}
OUTPUT_TYPES = ["clean", "main"]


@dataclass(order=True, frozen=True)
class DVCFile:
    path: Path
    hash: str
    stage: Stage

    @property
    def deps(self):
        return [
            Path(d.fs_path).relative_to(ROOT_DIR)
            for d in self.stage.deps
            if d.fs_path.startswith("/")
        ]

    @property
    def default_type(self):
        return DEFAULT_TYPES[self.base_dir]

    @property
    def default_format(self):
        return self.path.suffix[1:]

    @property
    def base_dir(self) -> str:
        parents = list(self.path.parents)
        assert parents[-2].resolve() == DATA_DIR and len(parents) >= 3
        return parents[-3].name

    @property
    def data_deps(self):
        return [p for p in self.deps if DATA_DIR in p.parents]

    @property
    def source_deps(self):
        return [p for p in self.deps if SRC_DIR in p.parents]

    @property
    def s3_url(self):
        hash_part = f"{URL_PREFIX}/{self.hash[:2]}/{self.hash[2:]}"
        return urljoin(CONFIG["s3_root"], hash_part)

    @property
    def http_url(self):
        hash_part = f"{URL_PREFIX}/{self.hash[:2]}/{self.hash[2:]}"
        return urljoin(CONFIG["http_root"], hash_part)

    @property
    def source_url(self):
        try:
            return next(
                d.fs_path for d in self.stage.deps if d.fs_path.startswith("http")
            )
        except StopIteration:
            return None

    def __repr__(self):
        return f"DataFile(path={str(self.path)!r})"

    def __str__(self):
        return str(self.path)


def get_data_files():
    fs = DVCFileSystem(".")
    index = fs.repo.index

    stages = index.stages

    for stage in stages:
        for out in stage.outs:
            yield DVCFile(
                Path(out.fs_path).relative_to(DATA_DIR.parent),
                out.hash_info.value,
                stage,
            )
