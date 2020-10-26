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
# split_data = parse.run()
# for training_example in split_data["train"]:
#     print(training_example)
#
# finding best attribute to split on and other data about entropies
# best_chess_attribute_data = DtreeMethods.find_best_attribute(split_data["train"])
# DtreeMethods.print_attribute_data(best_chess_attribute_data, CHESS_COLUMNS)


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


pie_dtree = DtreeMethods.build_tree(pie_data)

# shape_q_circle_child = pie_dtree.getChild("circle")
# shape_q_square_child = pie_dtree.getChild("square")
# shape_q_triangle_child = pie_dtree.getChild("triangle")
#
# print(type(shape_q_circle_child), shape_q_circle_child.getLabel())
# print(type(shape_q_square_child))
# print(type(shape_q_triangle_child), shape_q_triangle_child.getLabel())
#
# filling_q_big_child = shape_q_square_child.getChild("big")
# filling_q_small_child = shape_q_square_child.getChild("small")
#
# print(type(filling_q_big_child), filling_q_big_child.getLabel())
# print(type(filling_q_small_child), filling_q_small_child.getLabel())


example1 = ["6", "small", "square", "small", "neg"]

label = DtreeMethods.getClassification(pie_dtree, example1)
print("trying to print out label:", label)
