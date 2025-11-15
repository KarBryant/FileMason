import tomllib
from pathlib import Path

_config_cache = None

def load_config():
    global _config_cache

    if _config_cache is None:

        config_path = Path(__file__).parent / "config.toml"
        with open(config_path, "rb") as file:
            _config_cache = tomllib.load(file)
        
    return _config_cache
