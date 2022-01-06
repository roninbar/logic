from typing import Iterator

from Gate import Gate


class NotGate(Gate):
    _input: Gate

    def __init__(self, g: Gate):
        self._input = g

    def __str__(self):
        return f'(not {self._input})'

    def get_template(self, input_enum: Iterator[int]) -> str:
        return f'(not {self._input.get_template(input_enum)})'

    def get_output_value(self, input_iter: Iterator[str]) -> bool:
        return not self._input.get_output_value(input_iter)
