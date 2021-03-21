'''
Steps
1. Read data from data source
2. Save it in the data/raw for further processing
'''
import os
import argparse
import pandas as pd
from get_data import read_params, get_data

def load_and_save(config_path):
    # Load the df
    df = get_data(config_path)

    #Save the df as csv
    config = read_params(config_path)
    new_cols = [col.replace(" ", "_") for col in df.columns]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=",", index=False, header=new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()

    data = load_and_save(config_path=parsed_args.config)
