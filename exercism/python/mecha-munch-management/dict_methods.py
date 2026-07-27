"""Functions to manage a users shopping cart items."""

from typing import Dict, Iterable, List, Tuple


def add_item(
    current_cart: Dict[str, int], items_to_add: Iterable[str]
) -> Dict[str, int]:
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def read_notes(notes: Iterable[str]) -> Dict[str, int]:
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    return add_item({}, notes)


def update_recipes(
    ideas: Dict[str, Dict[str, int]], recipe_updates: Tuple[Tuple[str, Dict[str, int]]]
) -> Dict[str, Dict[str, int]]:
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart: Dict[str, int]):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(
    cart: Dict[str, int], aisle_mapping: Dict[str, List]
) -> Dict[str, List]:
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    return dict(
        sorted(
            (
                (item, [item_count, *aisle_mapping[item]])
                for item, item_count in cart.items()
            ),
            reverse=True,
        )
    )


def update_store_inventory(
    fulfillment_cart: Dict[str, List], store_inventory: Dict[str, List]
) -> Dict[str, List]:
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item, store_info in fulfillment_cart.items():
        stock = store_inventory[item][0]
        stock -= store_info[0]
        if stock == 0:
            stock = "Out of Stock"
        store_inventory[item][0] = stock

    return store_inventory
