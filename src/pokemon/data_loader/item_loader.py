from configparser import ConfigParser

from pokemon.schema import Item


class ItemLoader():
    def __init__(self, config_path: str):
        self._load_config(config_path)

    def _load_config(self, config_path: str):
        parser = ConfigParser()
        parser.read(config_path, 'utf-8')
        self._items: list[Item] = []
        for section in parser:
            if section == 'DEFAULT':
                continue

            self._items.append({
                'name': parser[section]['name'],
                'name_plural': parser[section]['nameplural'],
                'pocket': int(parser[section]['pocket']),
                'price': int(parser[section]['price']),
                'field_use': parser[section]['fielduse'],
                'flags': parser[section]['flags'].split(","),
                'description': parser[section]['description']
            })


if __name__ == '__main__':
    item_loader = ItemLoader("../../../PBS/items.ini")
