import pytest

import filemason.Config_Loader as config_loader
from filemason.Config_Loader import load_config
from filemason.Exceptions import (
    ConfigFileError,
    ConfigParseError,
    ConfigValidationError,
)


def test_config_not_cached():
    config_loader._config_cache = None
    assert config_loader._config_cache is None


def test_config_with_no_buckets(config_with_no_buckets, monkeypatch):
    config_loader._config_cache = None
    monkeypatch.setattr(
        config_loader, "config_path", config_with_no_buckets, raising=True
    )

    with pytest.raises(ConfigValidationError):
        load_config()


def test_load_config_multiple_extensions(config_with_multiple_extensions, monkeypatch):
    config_loader._config_cache = None
    monkeypatch.setattr(
        config_loader, "config_path", config_with_multiple_extensions, raising=True
    )

    with pytest.raises(ConfigValidationError):
        load_config()


def test_load_config_with_empty_bucket(config_with_empty_bucket, monkeypatch):
    config_loader._config_cache = None
    monkeypatch.setattr(
        config_loader, "config_path", config_with_empty_bucket, raising=True
    )

    with pytest.raises(ConfigValidationError):
        load_config()


def test_load_config_with_many_empty_buckets(
    config_with_many_empty_buckets, monkeypatch
):
    config_loader._config_cache = None
    monkeypatch.setattr(
        config_loader, "config_path", config_with_many_empty_buckets, raising=True
    )

    with pytest.raises(ConfigValidationError):
        load_config()


def test_load_config_happy_path(config, monkeypatch):
    config_loader._config_cache = None
    monkeypatch.setattr(config_loader, "config_path", config)
    data = load_config()
    assert data
    assert data["buckets"]
    assert len(data["buckets"]["images"]) == 3


def test_cached_config(config, monkeypatch):
    monkeypatch.setattr(config_loader, "config_path", config)

    config_info = load_config()
    assert config_info != None
    assert isinstance(config_info, dict)


def test_bad_toml_file(bad_toml_config, monkeypatch):
    config_loader._config_cache = None
    monkeypatch.setattr(config_loader, "config_path", bad_toml_config, raising=True)

    with pytest.raises(ConfigParseError):
        load_config()


def test_config_permissions_error(config, monkeypatch):
    config_loader._config_cache = None

    monkeypatch.setattr(config_loader, "config_path", config, raising=True)

    def raise_permission_error(*args, **kwargs):
        raise PermissionError("test error")

    monkeypatch.setattr("builtins.open", raise_permission_error)

    with pytest.raises(ConfigFileError):
        load_config()


def test_config_file_not_found(config, monkeypatch):
    config_loader._config_cache = None

    monkeypatch.setattr(config_loader, "config_path", config, raising=True)

    def raise_file_not_found_error(*args, **kwargs):
        raise FileNotFoundError("test error")

    monkeypatch.setattr("builtins.open", raise_file_not_found_error)

    with pytest.raises(ConfigFileError):
        load_config()


def test_config_file_os_error(config, monkeypatch):
    config_loader._config_cache = None

    monkeypatch.setattr(config_loader, "config_path", config, raising=True)

    def raise_file_os_error(*args, **kwargs):
        raise OSError("test error")

    monkeypatch.setattr("builtins.open", raise_file_os_error)

    with pytest.raises(ConfigFileError):
        load_config()
