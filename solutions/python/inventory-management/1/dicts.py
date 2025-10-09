"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory = dict()
    return add_items(inventory, items)


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if inventory.get(item, -1) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    inventory.pop(item, "none")
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_of_items = []
    for key, value in inventory.items():
        if value > 0:
            list_of_items.append(tuple([key, value]))
    return list_of_items

actual_result = list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0})
expected = [("coal", 15), ("diamond", 3), ("wood", 67)]
error_message = ('Called list_inventory({"coal": 15, "diamond": 3, "wood": 67, "silver": 0}). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected}.')
print(error_message)

actual_result = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond")
expected =  {"iron": 1, "gold": 1}
error_message = ('Called remove_item({"iron": 1, "diamond": 2, "gold": 1}, "diamond"). '
                         f'The function returned {actual_result}, but the tests expected {expected}.')
print(error_message)

actual_result = remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood")
expected = {"iron": 1, "gold": 1, "diamond": 2}
error_message = ('Called remove_item({"iron": 1, "diamond": 2, "gold": 1}, "wood"). '
                         f'The function returned {actual_result}, '
                         f'but the tests expected {expected}.')
print(error_message)