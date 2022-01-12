from functools import reduce
from typing import Iterator, Iterable, Callable, List

from Gate import Gate


class MultiGate(Gate):

    _inputs: list[Gate]
    _op: Callable[[bool, bool], bool]
    _initial: bool
    _opname: str

    def __init__(self, inputs: Iterable[Gate], op: Callable[[bool, bool], bool], initial: bool, opname: str):
        self._opname = opname
        self._initial = initial
        self._op = op
        self._inputs = list(inputs)

    def __str__(self):
        return f"({self._opname} {' '.join(str(input) for input in self._inputs)})"

    def template(self) -> str:
        return f"({self._opname} {' '.join(input.template() for input in self._inputs)})"

    def value(self, input_iter: Iterator[bool]) -> bool:
        return reduce(self._op, (input.value(input_iter) for input in self._inputs), self._initial)
