import argparse
import sys
from src.process import process_data
from src.process import process_files

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--input", type=str)
    # parser.add_argument("--output", type=str)
    # args = parser.parse_args()
    # process_data(args.input, args.output)

    input_files = sys.argv[1:]
    process_files(input_files)
