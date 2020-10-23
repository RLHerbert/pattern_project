from DtreeMethods import DtreeMethods
from enum import Enum
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

# parsing data into training set, holdout and validation
split_data = parse.run()
for training_example in split_data["train"]:
    print(training_example)

# finding best attribute to split on and other data about entropies
best_chess_attribute_data = DtreeMethods.find_best_attribute(split_data["train"])
DtreeMethods.print_attribute_data(best_chess_attribute_data, CHESS_COLUMNS)



