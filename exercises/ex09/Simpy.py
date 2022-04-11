"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730325952"


class Simpy:
    """Sequences of numerical data, version of NumPy."""
    values: list[float]

    def __init__(self, numbers: list[float]):
        """Constructor definition for initialization of attributes."""
        self.values = numbers

    def __str__(self) -> str:
        """Converting to str representation."""
        return f"Simpy({self.values})"

    def fill(self, value_filling: float, repeat: int) -> None:
        """Filling the values of the object."""
        self.values = []
        i: int = 0
        while i < repeat:
            self.values.append(value_filling)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Filling object with a range of values."""
        self.values = []
        assert step != 0.0
        while start < stop:
            self.values.append(start)
            start += step
        while start > stop:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """The sum of all the values."""
        result: float = 0.0
        for value in self.values:
            result += value
        return result

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the addition operator with an int value or object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.values.append(value + rhs)
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the power operator with an int value or object."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            for value in self.values:
                result.values.append(value ** rhs)
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checking if new float or object is equal to values in object."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checking if float or object is greater than values in object."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloading the subscription notation and producing new object based on boolean."""
        if isinstance(rhs, int):
            number: float = 0.0
            number += self.values[rhs]
            return number
        else:
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result
