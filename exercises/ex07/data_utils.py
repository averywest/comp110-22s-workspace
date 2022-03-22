"""Dictionary related utility functions."""

__author__ = ""

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(original: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Create new column based table with only the first few rows of each column."""
    first_rows: dict[str, list[str]] = {}
    for column in original:
        if N > len(original[column]):
            N = len(original[column])
        empty_list: list[str] = []
        x: int = 0 
        while x < N:
            empty_list.append(original[column][x])
            x += 1
        first_rows[column] = empty_list
    return first_rows


def select(primary: dict[str, list[str]], new: list[str]) -> dict[str, list[str]]:
    """Producing new column based table with a subset of the original columns."""
    new_dict: dict[str, list[str]] = {}
    for column in new:
        new_dict[column] = primary[column]
    return new_dict


def concat(initial: dict[str, list[str]], second_initial: dict[str, list[str]]) -> dict[str, list[str]]:
    """Producing column based table by combining two column based tables."""
    updated_dict: dict[str, list[str]] = {} 
    for column in initial:
        updated_dict[column] = initial[column]
    for column in second_initial:
        if column in updated_dict:
            x: int = 0
            while x < len(second_initial[column]):
                updated_dict[column].append(second_initial[column][x])
                x += 1
        else:
            updated_dict[column] = second_initial[column]
    return updated_dict


def count(frequency: list[str]) -> dict[str, int]:
    """Counting the number of times a value appears in an input list."""
    counter: dict[str, int] = {}
    for item in frequency:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter
