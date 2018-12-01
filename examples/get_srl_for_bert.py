# coding=utf-8

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import logging
import json
import glob
from os.path import join
from tqdm import tqdm
import pickle


logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(name)s -   %(message)s', 
                    datefmt = '%m/%d/%Y %H:%M:%S',
                    level = logging.INFO)
logger = logging.getLogger(__name__)


class InputFeatures(object):
    """A single set of features of data."""

    def __init__(self,
                 unique_id,
                 example_index,
                 doc_span_index,
                 tokens,
                 token_to_orig_map,
                 token_is_max_context,
                 input_ids,
                 input_mask,
                 segment_ids,
                 start_position=None,
                 end_position=None,
                 input_tags=None,
                 ):
        self.unique_id = unique_id
        self.example_index = example_index
        self.doc_span_index = doc_span_index
        self.tokens = tokens
        self.token_to_orig_map = token_to_orig_map
        self.token_is_max_context = token_is_max_context
        self.input_ids = input_ids
        self.input_mask = input_mask
        self.segment_ids = segment_ids
        self.start_position = start_position
        self.end_position = end_position
        self.input_tags = input_tags


def custom_key(file_name):
    key_numbers = []
    name = file_name.split('/')[-1]
    number = int(name[-5])
    if number == 0:
        number = 10
    key_numbers.append(number)
    return key_numbers


def main():
    parser = argparse.ArgumentParser()

    ## Required parameters
    parser.add_argument("--input_dir", default="/Users/will/Downloads/save_data", type=str)
    parser.add_argument("--output_dir", default="./save_data", type=str)
    parser.add_argument("--part_of_data", type=int, default=4)
    
    args = parser.parse_args()

    train_filenames = glob.glob(args.input_dir+"/train*")
    eval_filenames = glob.glob(args.input_dir+"/eval*")

    train_filenames.sort(key=custom_key)
    eval_filenames.sort(key=custom_key)

    train_features = []
    eval_features = []
    for train_file in train_filenames:
        with open(train_file, 'rb') as f:
            print("Loading data from "+(train_file.split("/"))[-1]+"...")
            features = pickle.load(f)
            train_features.extend(features)

    for eval_file in eval_filenames:
        with open(eval_file, 'rb') as f:
            print("Loading data from "+(eval_file.split("/"))[-1]+"...")
            features = pickle.load(f)
            eval_features.extend(features)

    def store_data(stored_features, output_file):
        output_data = {}
        for index, feature in tqdm(enumerate(stored_features), ncols=80, total=len(stored_features)):
            input_tags = [tag for tag in feature.input_tags if tag != 0]
            token_list = feature.tokens.copy()
            assert len(input_tags) == len(token_list)
            data = {"sentence_words":" ".join(token_list), "srl_tags":" ".join(input_tags)}
            output_data[index] = data

        with open(output_file, 'w') as json_file:
            json_file.write(json.dumps(output_data,sort_keys=True,indent=4))

    store_data(train_features, join(args.output_dir, "train_tags.json"))
    store_data(eval_features, join(args.output_dir, "dev_tags.json"))


if __name__ == "__main__":
    print("Start getting labels:")
    main()
    print("Process finished!")
