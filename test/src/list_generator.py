import random


def list_gen(list_size: int) -> list:
    """
    Function for generate list.
    :param list_size:int - size of the list
    :return result list
    """
    return [random.randrange(0, 100) for _ in range(0, list_size)]
