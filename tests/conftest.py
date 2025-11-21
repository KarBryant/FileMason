from services.Reader import Reader
from services.classifier import Classifier
import pytest
from pathlib import Path

@pytest.fixture
def classifier(buckets) -> Classifier:
    return Classifier(buckets)

@pytest.fixture
def reader() -> Reader:
    return Reader()


@pytest.fixture
def directory(tmp_path:Path) -> Path:
    dir:Path = tmp_path / "tmpdir"
    dir.mkdir()
    return dir

@pytest.fixture
def read_data(basic_dir):
    return Reader().read_directory(basic_dir)


@pytest.fixture
def config(directory) -> Path:
    config = directory / "config.toml"
    config.write_text(f"[buckets]\nimages = ['txt', 'jpeg', 'gif']")
    return config

@pytest.fixture
def bad_toml_config(directory):
    config = directory / "config.toml"
    config.write_text("test = [bad data,test]")
    return config

@pytest.fixture
def config_with_multiple_extensions(directory) -> Path:
    config = directory / "config.toml"
    config.write_text(f"[buckets]\nimages = ['png', 'jpeg', 'gif']\nvideos = ['png','mp4','mov']")
    return config

@pytest.fixture
def config_with_empty_bucket(directory):
    config = directory / "config.toml"
    config.write_text(f"[buckets]\nimages = []")
    return config

@pytest.fixture
def config_with_many_empty_buckets(directory):
    config = directory / "config.toml"
    config.write_text(f"[buckets]\nimages =[]\nvideos=[]")
    return config

@pytest.fixture
def config_with_no_buckets(directory):
    config = directory / "config.toml"
    config.write_text("images=['png']")
    return config


@pytest.fixture
def directory_with_subdir(directory:Path) -> Path:
    subdir = directory / "tmpsubdir"
    subdir.mkdir()

    return directory

@pytest.fixture
def symlink_dir(directory:Path) -> Path:

    base_file:Path = directory / "base.txt"
    base_file.write_text("test data")
    link:Path = directory / "link.txt"
    link.symlink_to(base_file)
    return directory

@pytest.fixture
def basic_dir(directory:Path) -> Path:
    file = directory / "test.txt"
    file.write_text("some data")

    return directory

@pytest.fixture
def multifile_dir(directory:Path) -> Path:
    file1 = directory / "test.txt"
    file1.write_text("some other data")
    file2 = directory / "test2.txt"
    file2.write_text("potatoes")
    
    return directory

@pytest.fixture
def hidden_file_dir(directory:Path) -> Path:
    file = directory / ".gitignore"
    file.write_text("env/")

    return directory

@pytest.fixture
def fifo_dir(directory: Path):
    import os
    os.mkfifo(directory / "mypipe")
    return directory
