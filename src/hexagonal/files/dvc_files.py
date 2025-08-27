from __future__ import annotations

from dataclasses import dataclass, field
from os.path import join
from pathlib import Path

from dvc.api import DVCFileSystem

from hexagonal.files import CONFIG
from hexagonal.files.spec import DatasetType, get_main_dir, relative_path

URL_PREFIX = "cache/files/md5"

DEFAULT_TYPES = {
    "01_raw": DatasetType.SOURCE,
    "02_clean": DatasetType.CLEAN,
    "03_main": DatasetType.MAIN,
}


@dataclass(order=True, frozen=True)
class DVCFile:
    path: Path
    hash: str
    deps: list[DVCFile] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)

    @property
    def default_type(self):
        return DEFAULT_TYPES[self.base_dir]

    @property
    def base_dir(self) -> str:
        return get_main_dir(self.path)

    @property
    def s3_url(self):
        hash_part = f"{URL_PREFIX}/{self.hash[:2]}/{self.hash[2:]}"
        return join(CONFIG["s3_root"], hash_part)

    @property
    def http_url(self):
        hash_part = f"{URL_PREFIX}/{self.hash[:2]}/{self.hash[2:]}"
        return join(CONFIG["http_root"], hash_part)

    def __repr__(self):
        return f"DVCFile(path={str(self.path)!r})"

    def __str__(self):
        return str(self.path)


def get_dvc_files() -> dict[Path, DVCFile]:
    fs = DVCFileSystem(".")
    index = fs.repo.index

    stages = index.stages

    files = {}
    deps = {}

    for stage in stages:
        for out in stage.outs:
            path = relative_path(out.fs_path)
            urls = [d.fs_path for d in stage.deps if d.fs_path.startswith("http")]
            files[path] = DVCFile(path, out.hash_info.value, urls=urls)
            deps[path] = [
                relative_path(d.fs_path)
                for d in stage.deps
                if d.fs_path.startswith("/")
            ]

    for path in deps:
        files[path].deps.extend(files[d] for d in deps[path] if d in files)

    return files
