import csv
import random


def data_to_array(row=[]):
    return [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]


def enumerate_data(enumerated=[]):
    temp = enumerated[1]
    temp.insert(0, enumerated[0])
    return temp


def parse():  # Opens the CSV file and parses it into a list of lists
    with open('data_set.csv', newline='\n') as data_set:
        # Creates list of lists from CSV
        data_reader = csv.reader(data_set, delimiter=',')
        # Assigns an ID to each vector then shuffles it
        shuffled = list(map(enumerate_data, list(enumerate(data_reader))))
        random.shuffle(shuffled)
        return shuffled


def run():  # Splits our data set into a training set, holdout set, and validation set
    shuffled_complete_data_set = parse()
    split_data_sets = {
        "train": shuffled_complete_data_set[:131],      # Training data set
        "holdt": shuffled_complete_data_set[132:175],   # Holdout data set
        "valid": shuffled_complete_data_set[176:]       # Validation data set
    }
    return split_data_sets


def main():
    print(run())
    # data_set = parse()
    # for row in data_set:
    #     print(row)


if __name__ == "__main__":
    main()
