from functools import reduce
from operator import methodcaller, and_
from typing import Iterator

from Gate import Gate


class AndGate(Gate):
    _inputs: list[Gate]

    def __init__(self):
        self._inputs = []

    def get_output_signal(self, input_iter: Iterator[str]) -> bool:
        input_signals = map(methodcaller('get_output_signal', input_iter), self._inputs)
        return reduce(and_, input_signals, True)

    def add_input(self, g: Gate):
        self._inputs.append(g)
