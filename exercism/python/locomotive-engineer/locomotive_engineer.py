"""Functions which helps the locomotive engineer to keep track of the train."""

from typing import Dict, List, Tuple


def get_list_of_wagons(*args: int) -> List[int]:
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """

    return [*args]


def fix_list_of_wagons(
    each_wagons_id: List[int], missing_wagons: List[int]
) -> List[int]:
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """

    wagon1, wagon2, locomotive, *rest_wagaons = each_wagons_id

    return [locomotive, *missing_wagons, *rest_wagaons, wagon1, wagon2]


def add_missing_stops(route: Dict[str, str], **stops) -> Dict[str, str | List[str]]:
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """

    return {**route, "stops": [*stops.values()]}


def extend_route_information(
    route: Dict[str, str], more_route_information: Dict[str, str]
) -> Dict[str, str]:
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """

    return {
        **route,
        **more_route_information,
    }  # can also be union '|', but not for the purpose of this exercise.


def fix_wagon_depot(
    wagons_rows: List[List[Tuple[int, str]]],
) -> List[List[Tuple[int, str]]]:
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """

    return [[*wagon_info] for wagon_info in zip(*wagons_rows)]
