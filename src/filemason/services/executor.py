from ..models.action_plan import ActionPlan
from ..models.action_step import Action
from filemason.exceptions import MoveError


class Executor:

    def handle(self, action_plan: ActionPlan):
        actions_taken = []
        failed_actions = []
        for step in action_plan.steps:
            if step.action == Action.mkdir:
                try:
                    step.destination.mkdir(exist_ok=True)
                    actions_taken.append(step)
                except FileNotFoundError as e:
                    failed_actions.append((step, e))
                except PermissionError as e:
                    failed_actions.append((step, e))
                except OSError as e:
                    failed_actions.append((step, e))
            elif step.action == Action.move:
                if step.source is None:
                    raise ValueError("Move commands must have a valid source.")
                try:
                    if step.destination.exists():
                        failed_actions.append(
                            (
                                step,
                                MoveError(
                                    "File of this name already exists in destination."
                                ),
                            )
                        )
                        continue
                    step.source.rename(step.destination)
                    actions_taken.append(step)
                except FileNotFoundError as e:
                    failed_actions.append((step, e))
                except PermissionError as e:
                    failed_actions.append((step, e))
                except OSError as e:
                    failed_actions.append((step, e))
        return actions_taken, failed_actions
