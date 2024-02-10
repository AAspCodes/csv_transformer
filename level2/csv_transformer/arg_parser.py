import argparse
from argparse import Namespace
import os

def get_args() -> Namespace:
# Create the parser
    parser = argparse.ArgumentParser(description='CSV CLI tool built in python for my dad.')
    
    # Add arguments
    parser.add_argument('-i', '--input', type=str, required=True, help='input file relative path')
    parser.add_argument('-o', '--output', type=str,required=True, help='output file relative path')
    parser.add_argument('-c', '--config', type=str, required=True, help='tranfrom config relative path')
    
    # Parse the arguments
    args = parser.parse_args()

    
    csv_ext = ".csv"
    yaml_ext = ".yaml"

    check_extension("input", args.input, csv_ext)
    check_extension("input", args.input, csv_ext)
    check_extension("config", args.config, yaml_ext)

    file_exists("input", str(args.input))
    file_exists("config", str(args.config))

    # Access and print the arguments
    print("Arguments Passed:")
    print(f"\tinput: {args.input}")
    print(f"\toutput: {args.output}")
    print(f"\ttransform config: {args.config}")
    return args



def check_extension(msg: str, path: str, ext: str):
    if not path.endswith(ext):
        print(f"Error: {msg} file does not have correct extension!")
        print(f"\texpected: {ext}, found: {path.split('.')[-1]}")
        print(f"\t{msg} passed: {path}")
        exit(1) # exit program with error



def file_exists(msg: str, path: str):
    if not os.path.exists(path):
        print(f"Error: {msg} file does not exist!")
        print(f"\t{msg} path passed: {path}")
        exit(1) # exit program with error

if __name__ == "__main__":
    # common to add this for testing
    # running python arg_parser.py with run just this file
    get_args()
