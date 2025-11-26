"""Domain model representing an ordered sequence of ActionSteps."""

from dataclasses import dataclass

from .action_step import ActionStep


@dataclass
class ActionPlan:
    """
    a collection of ActionSteps that will be executed by the Executor service.

    Attributes:
        steps: a list of ActionSteps for the Executor to execute in sequentail order.
    """

    steps: list[ActionStep]
