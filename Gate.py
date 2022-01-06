from abc import ABC, abstractmethod
from typing import Iterator


class Gate(ABC):

    @abstractmethod
    def get_template(self, input_enum: Iterator[int]) -> str:
        pass

    @abstractmethod
    def get_output_value(self, input_iter: Iterator[str]) -> bool:
        pass
