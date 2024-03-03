"""Creating functions with dictionary."""

__author__ = "730576169"

test_str: dict[str, str] = {"alice": "blue", "bob": "green", "steve": "blue"}
test_list: list[str] = ["steve", "steve", "bob", "bill", "bob"]

def invert(inv: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary of two strings."""
    for key in inv:
        new_inv: dict[str,str] = {inv[key]: key}
    if len(new_inv) != len(inv):
        raise KeyError("Duplicate Keys!")
    return new_inv


def favorite_color(color: dict[str, str]) -> str:
    """Picks the most popular color."""
    new_color: dict[str, int] = {}
    for key in color:
        key = color[key]
        if key in new_color:
            new_color[key] += 1
        else:
            new_color[key] = 1
    favorite_int: int = 0
    for key in new_color:
        if new_color[key] > favorite_int:
            favorite: str = key
            favorite_int = new_color[key]
    return favorite


def count(a: list[str]) -> dict[str, int]:
    """Counts how many of a str are in a list."""
    b:dict[str, int] = {}
    for key in a:
        if key in b:
            b[key] += 1
        else:
            b[key] = 1
    return b


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    "Groups strings by first letter."
    b:dict[str, list[str]] = {}
    for key in a:
        if key[0].lower() in b:
            b[key[0].lower()].append(key)
        else:
            b[key[0].lower()] = [key]
    return b



print(alphabetizer(test_list))