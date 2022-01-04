import yaml

# TODO: Parse the config file (logic.yaml)
with open('logic.yaml') as config_file:
    config = yaml.safe_load(config_file)

# TODO: Build all the gates and connect them to each other according to the config

with open('input.csv') as input_file:
    for input_line in input_file:
        pass  # Compute the output from the input line

