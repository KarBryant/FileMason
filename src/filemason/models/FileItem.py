"""Domain model for representing file metadata."""

from dataclasses import dataclass, field, replace
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from typing import List


@dataclass(frozen=True, slots=True)
class FileItem:
    """
    Immutable snapshot of a file's metadata.

    Attributes:
        id: Stable SHA256 hash based on path, size, and mtime.
        path: Absolute, normalized path to the file.
        name: File name without directory.
        extension: Lowercased file extension without leading dot.
        size: File size in bytes.
        created_at: Timezone-aware UTC creation timestamp.
        modified_at: Timezone-aware UTC last modified timestamp.
    """

    id: str = field(init=False)
    path: Path
    name: str
    extension: str
    size: int
    last_modified: datetime
    created: datetime
    tags: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        mtime_epoch = int(self.last_modified.timestamp())
        data = f"{self.path.as_posix()}{self.size}{mtime_epoch}".encode("utf-8")
        object.__setattr__(self, "id", sha256(data).hexdigest())

    def with_tag(self, tag) -> "FileItem":
        """
        Return a new FileItem with an additional tag.

        Args:
            tag: The tag to append to the existing tag list.

        Returns:
            A new FileItem instance with the given tag added.
        """
        return replace(self, tags=[*self.tags, tag])
