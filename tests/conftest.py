from pathlib import Path

import pytest

from filemason.services.reader import Reader
from filemason.services.classifier import Classifier
from filemason.services.planner import Planner
import filemason.config_loader as config_loader
from filemason.config_loader import load_config


@pytest.fixture
def reader() -> Reader:
    return Reader()


@pytest.fixture
def planner() -> Planner:
    return Planner()


@pytest.fixture
def classifier(buckets) -> Classifier:
    return Classifier(buckets)


@pytest.fixture
def directory(tmp_path: Path) -> Path:
    dir: Path = tmp_path / "tmpdir"
    dir.mkdir()
    return dir


@pytest.fixture
def config(directory) -> Path:
    config = directory / "config.toml"
    config.write_text("[buckets]\nimages = ['png', 'jpeg', 'gif']")
    return config


@pytest.fixture
def directory_with_subdir(directory: Path) -> Path:
    subdir = directory / "tmpsubdir"
    subdir.mkdir()

    return directory


@pytest.fixture
def read_data_with_bucket(dir_with_png):
    return Reader().read_directory(dir_with_png)


@pytest.fixture
def buckets(config, monkeypatch) -> dict:

    monkeypatch.setattr(config_loader, "config_path", config)

    config_data = load_config()
    return config_data


@pytest.fixture
def dir_with_png(directory: Path) -> Path:
    file = directory / "test.png"
    file.write_bytes(bytes(8))

    return directory


@pytest.fixture
def classifier_output(classifier, read_data_with_bucket):
    classified_list, unclassified_list = classifier.classify(read_data_with_bucket[0])
    return classified_list, unclassified_list


@pytest.fixture
def symlink_dir(directory: Path) -> Path:

    base_file: Path = directory / "base.txt"
    base_file.write_text("test data")
    link: Path = directory / "link.txt"
    link.symlink_to(base_file)
    return directory


@pytest.fixture
def basic_dir(directory: Path) -> Path:
    file = directory / "test.txt"
    file.write_text("some data")

    return directory


@pytest.fixture
def multifile_dir(directory: Path) -> Path:
    file1 = directory / "test.txt"
    file1.write_text("some other data")
    file2 = directory / "test2.txt"
    file2.write_text("potatoes")

    return directory


@pytest.fixture
def hidden_file_dir(directory: Path) -> Path:
    file = directory / ".gitignore"
    file.write_text("env/")

    return directory


@pytest.fixture
def fifo_dir(directory: Path):
    import os

    os.mkfifo(directory / "mypipe")
    return directory


@pytest.fixture
def plan(planner, basic_dir, buckets, classifier_output):
    classified, unclassified = classifier_output
    plan = planner.create_plan(
        base_output_path=basic_dir, files_list=classified, buckets=buckets
    )
    return plan
