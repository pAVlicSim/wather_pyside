import collections

from PySide6.QtWidgets import QComboBox


def add_city_history(his_list: collections.deque, box: QComboBox, loc: dict):
    try:
        his_list.append(loc['name'])
        box.clear()
        box.addItems(his_list)
    except KeyError:
        pass
