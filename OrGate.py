import operator
from typing import Iterable

from Gate import Gate
from MultiGate import MultiGate


class OrGate(MultiGate):

    def __init__(self, inputs: Iterable[Gate]):
        super(OrGate, self).__init__(inputs, operator.or_, False, 'or')
