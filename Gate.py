from abc import ABC, abstractmethod
from typing import Iterator


class Gate(ABC):

    @abstractmethod
    def template(self, input_enum: Iterator[int]) -> str:
        pass

    @abstractmethod
    def value(self, input_iter: Iterator[str]) -> bool:
        pass
