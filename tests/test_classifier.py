from services.classifier import Classifier
from services.Reader import Reader
from app.config_loader import load_config
import app.config_loader as config_loader
import pytest
from pathlib import Path

@pytest.fixture
def read_data_with_no_correct_bucket(basic_dir):
    return Reader().read_directory(basic_dir)

@pytest.fixture
def read_data_with_bucket(dir_with_png):
    return Reader().read_directory(dir_with_png)

@pytest.fixture
def buckets(config, monkeypatch) -> dict:

    monkeypatch.setattr(config_loader, "config_path",config)

    config_data = load_config()
    return config_data

@pytest.fixture
def classifier(buckets) -> Classifier:
    return Classifier(buckets)

@pytest.fixture
def dir_with_png(directory:Path) -> Path:
    file = directory / "test.png"
    file.write_bytes(bytes(8))

    return directory

def test_unclassified_file(classifier, read_data_with_no_correct_bucket):
   
    classified_list, unclassified_list = classifier.classify(read_data_with_no_correct_bucket[0])

    assert len(unclassified_list) == 2
    assert unclassified_list[0].extension == "toml"
    assert unclassified_list[0].tags == []
    assert classified_list == []

def test_classified_file(classifier, read_data_with_bucket):

    classified_list, unclassified_list = classifier.classify(read_data_with_bucket[0])

    assert len(classified_list) > 0
    assert classified_list[0].extension == "png"
    assert len(unclassified_list) == 1
    assert classified_list[0].tags == ['images']