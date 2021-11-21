import string
import os
import numpy as np
import pandas as pd

alpha_to_num_dict = dict(enumerate(string.ascii_lowercase))
num_to_alpha_dict = dict(zip(string.ascii_lowercase, range(0,26)))

def string_to_label(labels):
    """
    This function will return a string representing the label of a picture given
    the array label as input:
    Ex ouput: '1a', '4z' ...
    """
    label_temp = list(labels)
    label_temp = [int(x) for x in label_temp]
    number = label_temp[:10].index(1)
    letter = alpha_to_num_dict[label_temp[10:].index(1)]

    return str(number) + str(letter)


def label_to_string(letter_num):
    num, letter = int(letter_num[0]), letter_num[1].lower()
    numbers = [0 for i in range(10)]
    letters = [0 for i in range(26)]

    numbers[num] = 1
    letters[num_to_alpha_dict[letter]] = 1

    return ''.join([str(n) for n in numbers]) + ''.join([str(l) for l in letters])


test_folder = os.path.join(os.pardir, "data", "test")
unlabelled_folder = os.path.join(os.pardir, "data", "unlabelled")


def main():
    """
    Basically this script will look at the results of all models in the models list and will create a new
    csv file with predictions corresponding to the max vote that all models have said.
    """

    OUTPUT_CSV_PATH = "../ouput.csv"


    # t1 = pd.read_csv(os.path.join(test_folder, "best_test.csv"))
    # t2 = pd.read_csv(os.path.join(test_folder, "k.csv"))
    b1 = pd.read_csv(os.path.join(test_folder, "bag_1_test.csv"))
    b2 = pd.read_csv(os.path.join(test_folder, "bag_2_test.csv"))
    b3 = pd.read_csv(os.path.join(test_folder, "bag_3_test.csv"))
    b4 = pd.read_csv(os.path.join(test_folder, "bag_4_test.csv"))
    b5 = pd.read_csv(os.path.join(test_folder, "bag_5_test.csv"))

    models = [b1, b2, b3, b4, b5]

    final_df = pd.DataFrame(columns=["# Id", "Category"])

    num_non_conformity = 0

    for index, row in b1.iterrows():
        guesses = {}
        for model in models:
            guess = string_to_label(model.iloc[index].Category)
            if guess in guesses.keys():
                guesses[guess] += 1
            else:
                guesses[guess] = 1

        final_guess = max(guesses.items(), key=lambda b: b[1])[0]
        string_guess = label_to_string(final_guess)

        final_df = final_df.append({"# Id": index, "Category": string_guess}, ignore_index=True)

        if len(guesses) > 1:
            num_non_conformity += 1

    print(num_non_conformity)
    final_df.to_csv(OUTPUT_CSV_PATH, index=False)


if __name__ == "__main__":
    main()
