from Dtree import Dtree
from Driver import CHESS_COLUMNS
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
    return Dtree(dtree_2_train, CHESS_COLUMNS)


def main():
    tree_dict = parse.run()
    dtree = Dtree(tree_dict["train"], CHESS_COLUMNS)
    final = from_misclassified(tree_dict, dtree)


if __name__ == "__main__":
    main()
