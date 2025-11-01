from dataclasses import dataclass
from pathlib import Path
from enum import Enum


class Action(Enum):

    move = "MOVE"
    mkdir = "MKDIR"
    rename = "RENAME"

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class ActionStep:

    action: Action
    source: None | Path
    destination: None | Path


