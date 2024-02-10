# Serialization Deserialization
from typing import Dict

import yaml


def read_csv(path: str) -> list[list[str]]:
    with open(path, "r") as f:
        contents = f.read()

    out_list = []
    for line in contents.split("\n"):

        # skip final line of input file if empty
        if len(line) == 0:
            continue

        line_list = []
        for val in line.split(","):
            line_list.append(val)
        out_list.append(line_list)

    return out_list


def write_csv(data_to_write: list[list[str]], path: str):
    # convert 2D list of strings to a single string joined by "," and "\n"
    #   the inner list comprehension iterates over each row,
    #   takes the line: list[str], and converts it into a single string. with join
    #   the outer join takes the results list[str] where each string is was a row,
    #   and joins them all into single string

    #   Note: list comprehension do not mutate the list they iterate over,
    #       they copy and tranfrom and produce a new list
    #
    #   uncomment line below to see the intermediary step
    #   print([",".join(line) for line in data_to_write])
    #
    str_data = "\n".join([",".join(line) for line in data_to_write])
    with open(path, "w") as f:
        f.write(str_data)


def read_config(path: str) -> Dict:
    with open(path, "r") as f:
        config = yaml.safe_load(f.read())
    return config
