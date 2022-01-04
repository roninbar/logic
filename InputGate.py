from typing import Iterator

from Gate import Gate


class InputGate(Gate):

    def get_output_signal(self, input_iter: Iterator[str]) -> bool:
        s = next(input_iter).strip()
        return bool(int(s))
