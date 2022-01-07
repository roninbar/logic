from functools import reduce
from operator import methodcaller, and_
from typing import Iterator, Iterable

from Gate import Gate


class AndGate(Gate):
    _inputs: list[Gate]

    def __init__(self, inputs: Iterable[Gate] = None):
        self._inputs = list(inputs) if inputs else []

    def __str__(self):
        return f"(and {' '.join(str(input) for input in self._inputs)})"

    def template(self, input_enum: Iterator[int]) -> str:
        return f"(and {' '.join(input.template(input_enum) for input in self._inputs)})"

    def value(self, input_iter: Iterator[str]) -> bool:
        input_signals = map(methodcaller('value', input_iter), self._inputs)
        return reduce(and_, input_signals, True)

    def add_input(self, g: Gate):
        self._inputs.append(g)
