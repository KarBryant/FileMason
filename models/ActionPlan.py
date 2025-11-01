from dataclasses import dataclass
from models.ActionStep import ActionStep


@dataclass()
class ActionPlan:
    steps: list[ActionStep]
    summary: str = ""