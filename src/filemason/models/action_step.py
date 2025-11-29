"""Domain model for representing a singular action step to be taken"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class Action(Enum):
    """Enumeration of possible actions an ActionStep can perform."""

    move = "MOVE"
    mkdir = "MKDIR"
    rename = "RENAME"

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class ActionStep:
    """
    Domain model for a singular action step to be taken by the application.

    Attributes:
        id: The hashed ID of the FileItem
        action: The type of action to perform (move, mkdir, or rename).
        source: The source path relevant to the operation. May be None for mkdir.
        destination: The destination path relevant to the operation. May be None for rename.
    """

    file_id: str | None
    action: Action
    source: Path | None
    destination: Path
