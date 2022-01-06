from typing import Iterator

from Gate import Gate


class NotGate(Gate):
    _input: Gate

    def __init__(self, g: Gate):
        self._input = g

    def get_output_value(self, input_iter: Iterator[str]) -> bool:
        return not self._input.get_output_value(input_iter)
