"""Practice with dictionary functions."""

__author__ = "730325952"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary."""
    inverted_a: dict[str, str] = {}
    for key in a:
        inverted_a[a[key]] = key
    return inverted_a


def favorite_color(fun: dict[str, str]) -> str:
    """Determines what the most popular favorite color is."""
    popular_color: dict[str, int] = {}
    for key in fun:
        if fun[key] in popular_color:
            popular_color[fun[key]] += 1
        else:
            popular_color[fun[key]] = 1
    color: str = ""
    max_so_far: int = 0
    for key in popular_color:
        if popular_color[key] > max_so_far:
            max_so_far = popular_color[key]
            color = key
    return color
                                         

def count(unique_thing: list[str]) -> dict[str, int]:
    """Counts how many elements are repeated within a list by producing a dictionary."""
    counter: dict[str, int] = {}
    for unique in unique_thing:
        if unique in counter:
            counter[unique] += 1
        else:
            counter[unique] = 1
    return counter