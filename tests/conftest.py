from services.Reader import Reader
import pytest
from pathlib import Path


@pytest.fixture
def reader() -> Reader:
    return Reader()

@pytest.fixture
def directory(tmp_path:Path) -> Path:
    dir:Path = tmp_path / "tmpdir"
    dir.mkdir()
    return dir

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
