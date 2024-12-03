import pandas as pd
from os.path import splitext, basename


def process_data(infile, outfile):
    df = pd.read_parquet(infile)
    df.to_json(outfile, orient="records")


def process_files(input_list):
    for input in input_list:
        df = pd.read_parquet(input)

        output = basename(input)
        output = splitext(output)[0]
        output = f"/output/{output}.json"
        df.to_json(output, orient="records")
