'''
Steps
1. Split the raw dataset
2. Save it in data/processed folder
'''

import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]

    #split data
    df = pd.read_csv(raw_data_path, sep=",")
    train, test = train_data_path(df, test_size=split_ratio, random_state=random_state)

    #save data
    train.to_csv(train_data_path, sep=",", encoding='utf-8')
    test.to_csv(test_data_path, sep=",", encoding='utf-8')
