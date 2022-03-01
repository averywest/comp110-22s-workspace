"""Testing dictionary functions."""

__author__ = "730325952"

from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Edge case unit test for invert function."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_invert_letters() -> None:
    """Use case unit test for inverting dictionary."""
    a: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(a) == {"b": "a", "d": "c", "f": "e"}


def test_invert_words() -> None:
    """Use case unit test for inverting dictionary."""
    a: dict[str, str] = {"carrots": "celery", "raspberries": "blueberries", "lemonade": "tea"}
    assert invert(a) == {"celery": "carrots", "blueberries": "raspberries", "tea": "lemonade"}


def test_favorite_color_empty() -> None:
    """Edge case unit test for favorite color determination."""
    fun: dict[str, str] = {}
    assert favorite_color(fun) == ""


def test_favorite_color_normal() -> None:
    """Use case unit test for favorite color determination."""
    fun: dict[str, str] = {"Avery": "Green", "Taylor": "Green", "Abby": "Pink"}
    assert favorite_color(fun) == "Green"


def test_favorite_color_same() -> None:
    """Use case unit test for favorite color determination."""
    fun: dict[str, str] = {"Avery": "Green", "Taylor": "Green", "Abby": "pink", "Caidan": "blue", "Devin": "blue"}
    assert favorite_color(fun) == "Green"


def test_count_empty() -> None:
    """Edge case unit test to count elements in a list."""
    unique_thing: list[str] = ["apple"]
    assert count(unique_thing) == {"apple": 1}


def test_count_names() -> None:
    """Use case unit test to count elements in a list."""
    unique_thing: list[str] = ["Avery", "Abby", "Caidan", "Avery", "Abby", "Abby"]
    assert count(unique_thing) == {"Avery": 2, "Abby": 3, "Caidan": 1}


def test_count_flowers() -> None:
    """Use case unit test to count elements in a list."""
    unique_thing: list[str] = ["Carnation", "Tulip", "Carnation", "Carnation", "Carnation", "Carnation", "Carnation", "Carnation"]
    assert count(unique_thing) == {"Carnation": 7, "Tulip": 1}