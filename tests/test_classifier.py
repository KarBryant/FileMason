from services.classifier import Classifier
from app.config_loader import load_config
import app.config_loader as config_loader
import pytest

@pytest.fixture
def buckets(config, monkeypatch) -> dict:

    monkeypatch.setattr(config_loader, "config_path",config)

    config_data = load_config()
    return config_data

def test_classifier(read_data,buckets):
   
    classifier = Classifier(buckets)
    new_list = classifier.classify(read_data[0])

    assert len(new_list) > 0

    assert new_list[0].tags[0] == "images"