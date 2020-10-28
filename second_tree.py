from Dtree import Dtree
from enum import Enum
import parse
import random


def from_misclassified(tree_dict, dtree):
    boost_list = tree_dict["train"] + tree_dict["holdt"]
    for h in tree_dict["holdt"]:
        if (dtree.getClassification(h) != h[7]):
            boost_list.append(h)
            boost_list.append(h)
    dtree_2_train = []
    for _ in range(0, 132):
        dtree_2_train.append(boost_list[random.randint(0, len(boost_list))-1])
    # print(len(dtree_2_train))
    return Dtree(dtree_2_train, dtree.get_enum())


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
    dtree2 = from_misclassified(tree_dict, dtree1)
    print("Accuracy of dtree2:", dtree2.get_accuracy(tree_dict["holdt"]))

if __name__ == "__main__":
    main()
