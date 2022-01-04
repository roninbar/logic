from Gate import Gate


class AndGate(Gate):

    def __init__(self):
        self._inputs = []

    def get_output_signal(self):
        pass

    def add_input(self, g: Gate):
        self._inputs.append(g)
