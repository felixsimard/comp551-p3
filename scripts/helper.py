import string


alpha_to_num_dict = dict(enumerate(string.ascii_lowercase))
num_to_alpha_dict = dict(zip(string.ascii_lowercase, range(0,26)))

def list_to_label(labels):
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


def label_to_list(letter_num):
    """
    This function will return a list corresponding to the correct value it should be given a lable.
    """

    num, letter = int(letter_num[0]), letter_num[1].lower()
    numbers = [0 for i in range(10)]
    letters = [0 for i in range(26)]

    numbers[num] = 1
    letters[num_to_alpha_dict[letter]] = 1

    return ''.join([str(n) for n in numbers]) + ''.join([str(l) for l in letters])