import numpy as np
import pandas as pd
import pickle
import random

"""
This script can be used to create new datasets given an original one.
It implements the machine learning concept to decrease variance called bagging.

The original dataset is loaded, and NUM_NEW_DATASETS amount of datasets are created randomly with replacement.
They are then saved.
"""

def load_data(filename):
    loaded_pkl = None
    try:
        pkl_buffered = open(filename,'rb')
        loaded_pkl = pickle.load(pkl_buffered)
        pkl_buffered.close()
    except Exception as e:
        print("Error loading data: {}".format(e))
    return loaded_pkl


def main():
    NUM_NEW_DATASETS = 5
    original_data = load_data("../data/images_l.pkl")
    original_labels = load_data("../data/labels_l.pkl")

    for dataset in range(NUM_NEW_DATASETS):
        new_data = np.ndarray.copy(original_data)
        new_labels = np.ndarray.copy(original_labels)
        for i in range(len(original_data)):
            random_index = random.randrange(len(original_data))
            new_data[i] = original_data[random_index]
            new_labels[i] = original_labels[random_index]

        with open("../data/bagging_data/new_set_" + str(dataset) + ".pkl", "wb") as fp:
            pickle.dump(new_data, fp)
        with open("../data/bagging_data/new_set_" + str(dataset) + "_labels.pkl", "wb") as fp:
            pickle.dump(new_labels, fp)


if __name__ == "__main__":
    main()