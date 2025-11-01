"""Represents an immutable file metadata snapshot.
- path: expected to be absolute, resolved, and normalized.
- last_modified/created: timezone-aware UTC datetimes, microseconds stripped.
- id: SHA256 hash of normalized path, size, and mtime epoch."""


from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
from hashlib import sha256


@dataclass(frozen=True, slots=True)
class FileItem:
    id: str = field(init=False)
    path: Path
    name: str
    extension: str
    size: int
    last_modified: datetime
    created: datetime

    def __post_init__(self) -> None:
        mtime_epoch = int(self.last_modified.timestamp())
        data = f"{self.path.as_posix()}{self.size}{mtime_epoch}".encode('utf-8')
        object.__setattr__(
            self,'id', sha256(data).hexdigest()
        )
