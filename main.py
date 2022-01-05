import yaml
import csv

from AndGate import AndGate
from InputGate import InputGate
from NotGate import NotGate
from OrGate import OrGate


class ConfigError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{type(self)}: {self.message}'


def create_network(node):
    if node['type'] == 'term':
        gate = InputGate()
    elif node['type'] == 'not':
        gate = NotGate(create_network(node['input']))
    elif node['type'] == 'and':
        gate = AndGate(create_network(n) for n in node['inputs'])
    elif node['type'] == 'or':
        gate = OrGate(create_network(n) for n in node['inputs'])
    else:
        raise ConfigError(f"Invalid node type \"{node['type']}\"")

    return gate


with open('logic.yaml') as config_file:
    network = create_network(yaml.safe_load(config_file))

with open('input.csv') as input_file:
    for row in csv.reader(input_file):
        print(f'{[int(s) for s in row]} -> {int(network.get_output_signal(iter(row)))}')
