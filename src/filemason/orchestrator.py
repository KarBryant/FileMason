from filemason.services.classifier import Classifier
from filemason.services.executor import Executor
from filemason.services.planner import Planner
from filemason.services.reader import Reader
from filemason.models.run_result import RunResult
from pathlib import Path


class Orchestrator:

    def __init__(
        self,
        reader: Reader,
        classifier: Classifier,
        planner: Planner,
        executor: Executor,
        buckets: dict[str, list[str]],
    ):
        self.reader = reader
        self.classifier = classifier
        self.planner = planner
        self.executor = executor
        self.buckets = buckets

    def organize(self, directory: Path, dry_run: bool = True) -> RunResult:
        read_files, skipped_files = self.reader.read_directory(directory)
        classified_files, unclassified_files = self.classifier.classify(read_files)
        action_plan = self.planner.create_plan(
            directory, classified_files, self.buckets
        )

        if dry_run:
            return RunResult(
                source=directory,
                dry_run=dry_run,
                read_files=read_files,
                skipped_files=skipped_files,
                classified_files=classified_files,
                unclassified_files=unclassified_files,
                action_plan=action_plan,
                actions_taken=[],
                failed_actions=[],
            )

        successful_steps, failed_steps = self.executor.handle(action_plan)
        return RunResult(
            source=directory,
            dry_run=dry_run,
            read_files=read_files,
            skipped_files=skipped_files,
            classified_files=classified_files,
            unclassified_files=unclassified_files,
            action_plan=action_plan,
            actions_taken=successful_steps,
            failed_actions=failed_steps,
        )
