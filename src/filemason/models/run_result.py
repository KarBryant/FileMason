from dataclasses import dataclass
from filemason.models.file_item import FileItem
from filemason.models.action_step import ActionStep
from filemason.models.action_plan import ActionPlan
from pathlib import Path


@dataclass(frozen=True)
class RunResult:
    source: Path
    dry_run: bool
    read_files: list[FileItem]
    skipped_files: list[tuple[Path, str]]
    classified_files: list[FileItem]
    unclassified_files: list[FileItem]
    action_plan: ActionPlan
    actions_taken: list[ActionStep]
    failed_actions: list[tuple[ActionStep, Exception]]

    @property
    def total_files(self) -> int:
        return len(self.read_files)

    @property
    def success_count(self) -> int:
        return len(self.actions_taken)

    @property
    def failure_count(self) -> int:
        return len(self.failed_actions)
