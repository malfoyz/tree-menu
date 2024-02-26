from typing import Union, List, Tuple, Dict

from django import template

from src.menu.models import Menu, MenuItem


register = template.Library()


def update_tree_data(tree_data: List[tuple], path: str, depth=0):
    """
    Функция, добавляющая в древовидное меню для каждого элемента True
    1) если слаг элемента совпадает с путем path,
    2) для элементов перед элементом удовлетворящему условию 1.
    и False в противном случае.
    """
    if depth == 0:
        global is_opened
        is_opened = True
    for i in range(len(tree_data)):
        if tree_data[i][2] == path:
            global is_opened_count
            is_opened = False
            is_opened_count = depth
        if tree_data[i][3]:
            update_tree_data(tree_data[i][3], path, depth + 1)

        if 'is_opened_count' in globals() \
                and is_opened_count >= 0 and depth <= is_opened_count:
            tree_data[i] = tree_data[i] + (True,)
            is_opened_count -= 1
        else:
            tree_data[i] = tree_data[i] + (is_opened,)

    return tree_data


@register.inclusion_tag('menu/tags/menu.html', takes_context=True)
def menu(context: Dict, name: str):
    """Тег вывода меню по имени."""

    request = context.get('request')
    current_path = request.path.strip("/")

    items = Menu.get_ancestors_recursive(name)

    if items:
        items = update_tree_data(items, current_path)

    return {'items': items, 'current_path': current_path}


@register.inclusion_tag('menu/tags/subitems.html', True)
def subitems(subitems: List, current_path: str):
    """Тег вывода элементов родителя."""

    return {'items': subitems, 'current_path': current_path}
