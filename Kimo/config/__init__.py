import os
import json

_CONFIG_CACHE = None


def _find_config_file():
    """
    从当前文件开始，一层一层向上找 config.json
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        config_path = os.path.join(current_dir, "config.json")
        if os.path.exists(config_path):
            return config_path

        parent = os.path.dirname(current_dir)
        if parent == current_dir:  # 到根目录还没找到
            break
        current_dir = parent

    raise FileNotFoundError("在项目目录中未找到 config.json")


def load_config(section, key=None, default=None):
    global _CONFIG_CACHE

    if _CONFIG_CACHE is None:
        config_path = _find_config_file()
        print("使用配置文件:", config_path)

        with open(config_path, "r", encoding="utf-8") as f:
            _CONFIG_CACHE = json.load(f)

    if key is None:
        return _CONFIG_CACHE.get(section, default)

    return _CONFIG_CACHE.get(section, {}).get(key, default)
