import csv
import random


# Takes the enumeration of the row, a tuple, and places the id inside the list for convenience
def give_ids(enumerated=[]):
    row_with_id = enumerated[1]
    row_with_id.insert(0, str(enumerated[0]))
    return row_with_id


# Opens the CSV file and parses it into a list of lists
def parse():
    with open('data_set.csv', newline='\n') as data_set:
        # Creates list of lists from CSV
        data_reader = csv.reader(data_set, delimiter=',')
        # Assigns an ID to each vector then shuffles it
        shuffled = list(map(give_ids, list(enumerate(data_reader))))
        random.shuffle(shuffled)
        return shuffled


# Splits our data set into a training set, holdout set, and validation set
def run():
    shuffled_complete_data_set = parse()
    split_data_sets = {
        # Training data set
        "train": shuffled_complete_data_set[0:132],
        # Holdout data set
        "holdt": shuffled_complete_data_set[132:176],
        # Validation data set
        "valid": shuffled_complete_data_set[176:220]
    }
    return split_data_sets


def main():
    data = run()
    # print(data)
    print('Size of training set is 132: ' + str(len(data['train']) == 132))
    print('Size of holdout set is 44: ' + str(len(data['holdt']) == 44))
    print('Size of validation set is 44: ' + str(len(data['valid']) == 44))


if __name__ == "__main__":
    main()
