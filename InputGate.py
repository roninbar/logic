from typing import Iterator

from Gate import Gate


class InputGate(Gate):

    def __str__(self):
        return '(input)'

    def template(self) -> str:
        return '{}'

    def value(self, input_iter: Iterator[str]) -> bool:
        s = next(input_iter).strip()
        return bool(int(s))
