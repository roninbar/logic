import yaml

from AndGate import AndGate
from InputGate import InputGate
from NotGate import NotGate
from OrGate import OrGate

with open('logic.yaml') as config_file:
    config = yaml.safe_load(config_file)


class ConfigError(Exception):
    def __init__(self, message):
        self.message = message


def create_network(node):
    match node['type']:
        case 'term':
            gate = InputGate()
        case 'not':
            gate = NotGate(create_network(node['input']))
        case 'and':
            gate = AndGate()
            for n in node['inputs']:
                gate.add_input(create_network(n))
        case 'or':
            gate = OrGate()
            for n in node['inputs']:
                gate.add_input(create_network(n))
        case _:
            raise ConfigError(f"Invalid node type \"{node['type']}\"")

    return gate


network = create_network(config)

with open('input.csv') as input_file:
    for input_line in input_file:
        print(network.get_output_signal())
