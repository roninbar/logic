from functools import reduce
from operator import methodcaller, or_
from typing import Iterator, Iterable

from Gate import Gate


class OrGate(Gate):
    _inputs: list[Gate]

    def __init__(self, inputs: Iterable[Gate] = []):
        self._inputs = list(inputs)

    def get_output_signal(self, input_iter: Iterator[str]) -> bool:
        input_signals = map(methodcaller('get_output_signal', input_iter), self._inputs)
        return reduce(or_, input_signals, False)

    def add_input(self, g: Gate):
        self._inputs.append(g)
