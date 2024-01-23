from configparser import ConfigParser
import re
from typing import Optional, Iterator


class IniData():
    def __init__(self, config_path: str):
        self._load_config(config_path)

    def _load_config(self, config_path: str):
        """
        parser = ConfigParser()
        parser.read(config_path, 'utf-8')
        self._items: list[dict[str, str]] = []
        for section in parser:
            if section == 'DEFAULT':
                continue

            items = parser.items(section)
            self._items.append(dict(items))
            """

        with open(config_path, 'r', encoding='utf') as file:
            self._items: dict[str, dict[str, str]] = {}
            item_id: Optional[str] = None
            for line in file:
                if line.startswith('#'):
                    continue

                match = re.match(r'\[(\w+)]', line)
                if match is not None:
                    item_id = match.group(1)
                    self._items[item_id] = {}

                match = re.match(r'(\w+)\s*=\s*(.*)', line)
                if match is not None and item_id is not None:
                    key = match.group(1)
                    value = match.group(2)
                    self._items[item_id][key] = value

    def __iter__(self) -> Iterator[tuple[str, dict[str, str]]]:
        return iter(self._items.items())


if __name__ == '__main__':
    item_loader = IniData("../../../PBS/items.ini")
    for item in item_loader:
        print(item)
