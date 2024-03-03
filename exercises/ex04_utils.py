"""Utilzing functons and lists."""

__author__ = "730576169"


listy: list[int] = [1, 1]
listi: list[int] = [1, 1, 2]


def all(list_a: list[int], a: int) -> bool:
    """Checks if all ints match the given int."""
    index: int = 0
    loop_end: bool = True
    while index < len(list_a) and loop_end:
        if len(list_a) == 0:
            return False
        if list_a[index] == a:
            index += 1
            if index == len(list_a):
                return True
        else:
            loop_end = False
    return False


def max(list_b: list[int]) -> int:
    """Returns the maximum int in a list."""
    if len(list_b) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    max_value: int = list_b[index]
    while index < len(list_b):
        if max_value < list_b[index]:
            max_value = list_b[index]
            index += 1
        else:
            index += 1
    return max_value


def is_equal(list_c: list[int], list_d: list[int]) -> bool:
    """Tests if every element at is equal at the every index."""
    if len(list_c) != len(list_d):
        return False
    elif len(list_c) <= len(list_d):
        index_a: int = 0
        if len(list_c) == 0 and len(list_d) == 0:
            return True
        elif len(list_c) == 0 or len(list_d) == 0:
            return False
        while index_a < len(list_d):
            if list_c[index_a] == list_d[index_a]:
                index_a += 1
                if index_a == len(list_d):
                    return True
            else:
                return False
    else:
        if len(list_c) == 0 and len(list_d) == 0:
            return True
        elif len(list_c) == 0 or len(list_d) == 0:
            return False
        index_b: int = 0
        while index_b < len(list_c):
            if list_c[index_b] == list_d[index_b]:
                index_b += 1
                if index_b == len(list_c):
                    return True
            else:
                return False
    return False
        

def extend(list_e: list[int], list_f: list[int]) -> None:
    """Extends a list by adding another to the end of it."""
    index = 0
    while index < len(list_f):
        list_e.append((list_f[index]))
        index += 1


is_equal(listy, listi)