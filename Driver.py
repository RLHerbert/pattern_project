from DtreeMethods import DtreeMethods
from enum import Enum
import random
import parse


class CHESS_COLUMNS(Enum):
    NO_ATTRIBUTE = -1
    ID = 0
    WHITE_KING_FILE = 1
    WHITE_KING_RANK = 2
    WHITE_ROOK_FILE = 3
    WHITE_ROOK_RANK = 4
    BLACK_KING_FILE = 5
    BLACK_KING_RANK = 6
    CLASS = 7

# CHESS TEST*****************************************:
# parsing data into training set, holdout and validation
split_data = parse.run()
# for training_example in split_data["train"]:
#     print(training_example)

# make the chess dtree
chess_dtree = DtreeMethods.build_tree(split_data["train"])
# get possible classes
possible_labels = DtreeMethods.get_possible_labels_from_data(split_data["train"])
# test example, this is the first example from csv file. class should be draw
chess_example1 = ['1', 'd', '1', 'f', '3', 'e', '4', '???']
# this other example should be class 'five'
chess_example112 = ['112', 'd', '3', 'c', '4', 'c', '1', '???']
# get the classifications
print("classification of example 1 from chess dtree is:",
      DtreeMethods.getClassification(chess_dtree, chess_example1, possible_labels))
print("classification of example 122 from chess dtree is:",
      DtreeMethods.getClassification(chess_dtree, chess_example112, possible_labels))


# PIE TEST*****************************************:
class PIE_COLUMNS(Enum):
    NO_ATTRIBUTE = -1
    ID = 0
    CRUST_SIZE = 1
    SHAPE = 2
    FILLING_SIZE = 3
    CLASS = 4


pie_data = [
        ["1", "big", "circle", "small", "pos"],
        ["2", "small", "circle", "small", "pos"],
        ["3", "big", "square", "small", "neg"],
        ["4", "big", "triangle", "small", "neg"],
        ["5", "big", "square", "big", "pos"],
        ["6", "small", "square", "small", "neg"],
        ["7", "small", "square", "big", "pos"],
        ["8", "big", "circle", "big", "pos"],
    ]


# build the dtree
pie_dtree = DtreeMethods.build_tree(pie_data)
possible_labels = ["pos", "neg"]

# test example. should be negative
example1 = ["6", "small", "square", "small", "???"]

# classify the test example
print("classification from pie dtree is:", DtreeMethods.getClassification(pie_dtree, example1, possible_labels))
