from abc import ABC, abstractmethod


class Gate(ABC):

    @abstractmethod
    def get_output_signal(self):
        pass
