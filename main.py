import csv

import yaml

from AndGate import AndGate
from InputGate import InputGate
from NotGate import NotGate
from OrGate import OrGate


class ConfigError(Exception):

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return f'{type(self)}: {self._message}'


def create_network(node):
    if node['type'] == 'term':
        return InputGate()
    elif node['type'] == 'not':
        return NotGate(create_network(node['input']))
    elif node['type'] == 'and':
        return AndGate(create_network(n) for n in node['inputs'])
    elif node['type'] == 'or':
        return OrGate(create_network(n) for n in node['inputs'])
    else:
        raise ConfigError(f"Invalid node type \"{node['type']}\"")


with open('logic.yaml') as config_file:
    network = create_network(yaml.safe_load(config_file))

print(network)

with open('input.csv') as input_file:
    for row in csv.reader(input_file):
        template = network.template()
        value = network.value(iter(row))
        print(template.format(*[int(s) for s in row]) + ' = ' + str(int(value)))
