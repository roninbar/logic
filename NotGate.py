from Gate import Gate


class NotGate(Gate):
    _input: Gate

    def __init__(self, g: Gate):
        self._input = g

    def get_output_signal(self):
        return not self._input.get_output_signal()
