from enum import Enum
from Dtree import Dtree
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
chess_dtree = Dtree(split_data["train"], CHESS_COLUMNS)
# chess_dtree.output_q_node_data()
# chess_dtree.output_leaf_node_data()
# chess_dtree.output_parents()
# chess_dtree.output_everything()
# test example, this is the first example from csv file. class should be draw
chess_example1 = ['1', 'd', '1', 'f', '3', 'e', '4', '???']
# this other example should be class 'five'
chess_example112 = ['112', 'd', '3', 'c', '4', 'c', '1', '???']
# get the classifications
print("classification of example 1 from chess dtree is:", chess_dtree.getClassification(chess_example1))
print("classification of example 122 from chess dtree is:", chess_dtree.getClassification(chess_example112))


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
pie_dtree = Dtree(pie_data, PIE_COLUMNS)
# pie_dtree.output_q_node_data()
# pie_dtree.output_leaf_node_data()
# pie_dtree.output_parents()
pie_dtree.output_everything()


# test example. should be negative
example1 = ["6", "small", "square", "small", "???"]

# classify the test example
print("classification from pie dtree is:", pie_dtree.getClassification(example1))
