"""Practicing Unit Testing."""

__author__ = "730325952"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_odds() -> None:
    numbers: list[int] = [1, 3, 5]
    assert only_evens(numbers) == []


def test_only_evens_many_numbers() -> None:
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert only_evens(numbers) == [2, 4, 6, 8, 10, 12, 14]


def test_sub_empty() -> None:
    numbers_two: list[int] = []
    assert sub(numbers_two, 1, 3) == []


def test_sub_correct() -> None:
    numbers_two: list[int] = [10, 20, 30, 40, 50, 60]
    assert sub(numbers_two, 3, 5) == [40, 50]


def test_sub_absurd_numbers() -> None:
    numbers_two: list[int] = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert sub(numbers_two, -200, 200) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


def test_concat_empty() -> None:
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_single_items() -> None:
    first_list: list[int] = [5]
    second_list: list[int] = [10]
    assert concat(first_list, second_list) == [5, 10]


def test_concat_many_items() -> None:
    first_list: list[int] = [1, 2, 3, 4, 5]
    second_list: list[int] = [6, 7, 8, 9, 10]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]