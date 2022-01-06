import argparse
import csv
from sys import stdin

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
    match node:
        case {'type': 'term'}:
            gate = InputGate()
        case {'type': 'not', 'input': input}:
            gate = NotGate(create_network(input))
        case {'type': 'and', 'inputs': inputs}:
            gate = AndGate(create_network(input) for input in inputs)
        case {'type': 'or', 'inputs': inputs}:
            gate = OrGate(create_network(input) for input in inputs)
        case {'type': type}:
            raise ConfigError(f"Invalid node type \"{type}\"")

    return gate


parser = argparse.ArgumentParser(description='Evaluate a Boolean function.')
parser.add_argument('--config', '-c',
                    dest='config',
                    default='config.yaml',
                    help='Path of YAML file describing the function.')
args = parser.parse_args()

with open(args.config) as config_file:
    network = create_network(yaml.safe_load(config_file))

print(network)

template = network.template()

for row in csv.reader(stdin):
    try:
        value = network.value(bool(int(value.strip())) for value in row)
        print(template.format(*[int(s) for s in row]) + ' = ' + str(int(value)))
    except IndexError:
        print(f'! Insufficient inputs: ')
