from functools import reduce
from operator import methodcaller, and_
from typing import Iterator, Iterable

from Gate import Gate


class AndGate(Gate):
    _inputs: list[Gate]

    def __init__(self, inputs: Iterable[Gate] = []):
        self._inputs = list(inputs)

    def get_output_value(self, input_iter: Iterator[str]) -> bool:
        input_signals = map(methodcaller('get_output_value', input_iter), self._inputs)
        return reduce(and_, input_signals, True)

    def add_input(self, g: Gate):
        self._inputs.append(g)
