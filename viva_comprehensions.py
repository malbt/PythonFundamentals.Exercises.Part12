from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:

    """
    write a function to find the parity of a given number
    :param start: The first int inclusive.
    :param stop: The last int exclusive.
    :param parity: specifying odd and even
    :return: list of numbers in range of parity
    """

    return [num for num in range(start, stop) if num % 2 != parity.value]


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    write a function that generates integers with a manipulating function in it
    :param start: starting integer in a dictionary (inclusive)
    :param stop: ending  integer in a dictionary (exclusive)
    :param strategy:A function to manipulate each digit
    :return: a dictionary integer
    """
    return {num: strategy(num) for num in range(start, stop)}


def gen_set(val_in: str) -> Set:
    """
    write a function that changes string to upper case
    :param val_in: string
    :return: upper case list
    """
    return {word.upper() for word in val_in if word == word.lower()}
