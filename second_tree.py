"""
second_tree.py - Class that returns the information about the second dtree
Namely returns the second dtree, its training set, and the misclassified holdouts of dtree1

Dennis La - Dennis.La@student.csulb.edu
Melissa Hazlewood - Melissa.Hazlewood@student.csulb.edu
Rowan Herbert - Rowan.Herbert@student.csulb.edu
Sophanna Ek - Sophanna.Ek@student.csulb.edu
"""
from Dtree import Dtree
from enum import Enum
import parse
import random


def from_misclassified(tree_dict, dtree):
    """
    Function that creates a second dtree
    :param tree_dict: the dataset split up into train,
    :param dtree: the first dtree
    :return: the second dtree, its training set, and the misclassified holdouts of dtree1
    """

    boost_list = tree_dict["train"] + tree_dict["holdt"]
    misclassified = []
    num_columns = len(boost_list[0])
    for h in tree_dict["holdt"]:
        if (dtree.get_classification(h) != h[num_columns - 1]):
            misclassified.append(h)
            boost_list.append(h)
            boost_list.append(h)
    dtree_2_train = []
    for _ in range(0, len(tree_dict["train"])):
        dtree_2_train.append(boost_list[random.randint(0, len(boost_list))-1])
    # print(len(dtree_2_train))
    dtree_2_dict = {
        "dtree": Dtree(dtree_2_train, dtree.get_enum()),
        "train": dtree_2_train,
        "miscl": misclassified
    }
    return dtree_2_dict


def main():
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

    tree_dict = parse.run()
    dtree1 = Dtree(tree_dict["train"], CHESS_COLUMNS)
    print("Accuracy of dtree1:", dtree1.get_accuracy(tree_dict["holdt"]))
    dtree2 = from_misclassified(tree_dict, dtree1)["dtree"]
    print("Accuracy of dtree2:", dtree2.get_accuracy(tree_dict["holdt"]))


if __name__ == "__main__":
    main()
