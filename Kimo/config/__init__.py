import json
_CONFIG_CACHE = None

def load_config(config_type, value, default=None):
    global _CONFIG_CACHE

    if _CONFIG_CACHE is None:
        with open("./config.json", "r", encoding="utf-8") as f:
            _CONFIG_CACHE = json.load(f)

    return _CONFIG_CACHE.get(config_type, {}).get(value, default)