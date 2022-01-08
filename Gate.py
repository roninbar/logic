from abc import ABC, abstractmethod
from typing import Iterator


class Gate(ABC):

    @abstractmethod
    def template(self) -> str:
        pass

    @abstractmethod
    def value(self, input_iter: Iterator[str]) -> bool:
        pass
