import random
from enum import Enum
import parse
from Dtree import Dtree
from second_tree import from_misclassified


class DtreeEnsemble:
    def __init__(self):
        # list of trees
        self.__list_of_dtrees = []

    def add_dtree_to_ensemble(self, dtree_to_add):
        self.__list_of_dtrees.append(dtree_to_add)

    def get_voting_results(self, example):
        vote_weight_dict = {}

        # go through each d tree and ask it to classify the example.
        # then create a key with the label it gives for the example
        # store each key (label) with a running total of weights of trees that vote for that label
        for dtree in self.__list_of_dtrees:
            label = dtree.getClassification(example)
            if label in vote_weight_dict:
                vote_weight_dict[label] += dtree.get_voting_weight()
            else:
                vote_weight_dict[label] = dtree.get_voting_weight()

        # find the max voting weight in vote weight dict
        # let the max be a random label
        label_with_max_vote_weight = random.choice(list(vote_weight_dict))
        for label in vote_weight_dict:
            if vote_weight_dict[label] > vote_weight_dict[label_with_max_vote_weight]:
                # found a new max
                label_with_max_vote_weight = label

        return label_with_max_vote_weight

    def get_accuracy(self, dataset):
        correct = 0
        for example in dataset:
            if example[len(dataset[0]) - 1] == self.get_voting_results(example):
                correct += 1
        return correct / len(dataset)


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

    # test example, this is the first example from csv file. class should be draw
    chess_example1 = ['1', 'd', '1', 'f', '3', 'e', '4', '???']
    # this other example should be class 'five'
    chess_example112 = ['112', 'd', '3', 'c', '4', 'c', '1', '???']

    tree_dict = parse.run()
    dtree1 = Dtree(tree_dict["train"], CHESS_COLUMNS)
    dtree1_acc = dtree1.get_accuracy(tree_dict["holdt"])
    print("Accuracy of dtree1:", dtree1_acc)

    dtree2 = from_misclassified(tree_dict, dtree1)
    dtree2_acc = dtree2.get_accuracy(tree_dict["holdt"])

    print("Accuracy of dtree2:", dtree2_acc)
    dtree_ensemble = DtreeEnsemble()
    dtree1.set_voting_weight(dtree1_acc)
    dtree2.set_voting_weight(dtree2_acc)
    dtree_ensemble.add_dtree_to_ensemble(dtree1)
    dtree_ensemble.add_dtree_to_ensemble(dtree2)

    print()
    print("classification of example 1 from dtree1 is:", dtree1.getClassification(chess_example1))
    #print("classification of example 122 from dtree1 is:", dtree1.getClassification(chess_example112))

    print()
    print("classification of example 1 from dtree2 is:", dtree2.getClassification(chess_example1))
    #print("classification of example 122 from dtree2 is:", dtree2.getClassification(chess_example112))

    print()
    print("classification of example 1 from ensemble is:", dtree_ensemble.get_voting_results(chess_example1))
    #print("classification of example 122 from ensemble is:", dtree_ensemble.get_voting_results(chess_example112))

if __name__ == "__main__":
    main()
