"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first_wagon, second_wagon, locomotive, *rest_of_train = each_wagons_id
    return [locomotive, *missing_wagons, *rest_of_train, first_wagon, second_wagon]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    return {**route, "stops": list(kwargs.values())}


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the wagon depot using unpacking.

    :param wagons_rows: list[list[tuple]] - list of rows of wagons
    :return: list[list[tuple]] - fixed list of rows
    """
    row1, row2, row3 = wagons_rows
    r1a, r1b, r1c = row1
    r2a, r2b, r2c = row2
    r3a, r3b, r3c = row3
    new_row1 = [r1a, r2a, r3a]
    new_row2 = [r1b, r2b, r3b]
    new_row3 = [r1c, r2c, r3c]
    return [new_row1, new_row2, new_row3]

