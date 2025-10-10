"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item_to_add in items_to_add:
        current_cart.setdefault(item_to_add, 0)
        current_cart[item_to_add] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(dict(recipe_updates))
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fullfilment_cart = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            new_value = [quantity, aisle_mapping[item][0], aisle_mapping[item][1]]
            fullfilment_cart.setdefault(item, new_value)
    return dict(reversed(sorted(fullfilment_cart.items())))


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key_cart, value_cart in fulfillment_cart.items():
        if store_inventory.get(key_cart, -1) != -1:
            store_inventory[key_cart][0] -= value_cart[0]
            if store_inventory[key_cart][0] <= 0:
                store_inventory[key_cart][0] = "Out of Stock"
    return store_inventory

