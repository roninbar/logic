from functools import reduce
from operator import methodcaller, or_
from typing import Iterator, Iterable

from Gate import Gate


class OrGate(Gate):
    _inputs: list[Gate]

    def __init__(self, inputs: Iterable[Gate]):
        self._inputs = list(inputs) if inputs else []

    def __str__(self):
        return f"(or {' '.join(str(input) for input in self._inputs)})"

    def template(self) -> str:
        return f"(or {' '.join(input.template() for input in self._inputs)})"

    def value(self, input_iter: Iterator[bool]) -> bool:
        input_signals = map(methodcaller('value', input_iter), self._inputs)
        return reduce(or_, input_signals, False)

    def add_input(self, g: Gate):
        self._inputs.append(g)
