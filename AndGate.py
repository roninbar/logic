import operator
from typing import Iterable

from Gate import Gate
from MultiGate import MultiGate


class AndGate(MultiGate):

    def __init__(self, inputs: Iterable[Gate]):
        super(AndGate, self).__init__(inputs, operator.and_, False, 'and')

