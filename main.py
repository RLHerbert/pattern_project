"""
main.py - The entry point of the project. prints out all the output
for the project

Dennis La - Dennis.La@student.csulb.edu
Melissa Hazlewood - Melissa.Hazlewood@student.csulb.edu
Rowan Herbert - Rowan.Herbert@student.csulb.edu
Sophanna Ek - Sophanna.Ek@student.csulb.edu
"""
from Dtree import Dtree
from Ensemble import DtreeEnsemble
from enum import Enum
import parse
from second_tree import from_misclassified


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


def main():
    # parse the data
    tree_data_dictionary = parse.run()

    # create the first tree
    dtree_1 = Dtree(tree_data_dictionary["train"], CHESS_COLUMNS)
    # create the second tree
    dtree_2_dict = from_misclassified(tree_data_dictionary, dtree_1)

    # print training, holdout, and validation sets for dtree_1
    print("********************************START OF DTREE 1 DATASET DETAILS********************************")
    print("Training set:")
    for elem in tree_data_dictionary["train"]:
        print(elem)
    print("Holdout set:")
    for elem in tree_data_dictionary["holdt"]:
        print(elem)
    print("Validation set:")
    for elem in tree_data_dictionary["valid"]: 
        print(elem)
    print("********************************END OF DTREE 1 DATASET DETAILS********************************")

    # print training, holdout, and validation sets for dtree_2
    print("********************************START OF DTREE 2 DATASET DETAILS********************************")
    print("Training set:")
    for elem in dtree_2_dict["train"]:
        print(elem)
    print("Holdout set: (same as Dtree 1)")
    for elem in tree_data_dictionary["holdt"]:
        print(elem) 
    print("Validation set: (same as Dtree 1)")
    for elem in tree_data_dictionary["valid"]:
        print(elem) 
    print("********************************END OF DTREE 2 DATASET DETAILS********************************")

    print("********************************START OF DTREE 1 CONSTRUCTION DETAILS********************************")
    dtree_1.output_everything()
    print("*********************************END OF DTREE 1 CONSTRUCTION DETAILS*********************************")

    print()

    dtree_2 = dtree_2_dict["dtree"]
    print("********************************START OF DTREE 2 CONSTRUCTION DETAILS********************************")
    dtree_2.output_parents()
    print("*********************************END OF DTREE 2 CONSTRUCTION DETAILS*********************************")

    print()

    # print misclassified holdout vectors for the first tree
    print("********************************START OF DTREE 1 MISCLASSIFIED********************************")
    for elem in dtree_2_dict["miscl"]:
        print(elem) 
    print("********************************END OF DTREE 1 MISCLASSIFIED********************************")

    print()

    print("********************************START OF HOLDOUT ACCURACY********************************")
    # printing accuracies based on hold out set
    accuracy_of_dtree_1_on_holdt = dtree_1.get_accuracy(
        tree_data_dictionary["holdt"])
    accuracy_of_dtree_2_on_holdt = dtree_2.get_accuracy(
        tree_data_dictionary["holdt"])
    print("Error rate of Dtree 1 on holdout set:",
          (1 - accuracy_of_dtree_1_on_holdt) * 100, "%")
    print("Error rate of Dtree 2 on holdout set:",
          (1 - accuracy_of_dtree_2_on_holdt) * 100, "%")
    print("********************************END OF HOLDOUT ACCURACY********************************")

    print()

    print("********************************START OF VOTING WEIGHT********************************")
    # setting the voting weights as the accuracies on original data set
    original_set = tree_data_dictionary["train"] + tree_data_dictionary["holdt"] + tree_data_dictionary["valid"]
    dtree_1.set_voting_weight(dtree_1.get_accuracy(original_set))
    dtree_2.set_voting_weight(dtree_2.get_accuracy(original_set))
    print()
    print("Voting weight of Dtree 1 (based on accuracy):",
          dtree_1.get_voting_weight())
    print("Voting weight of Dtree 2 (based on accuracy):",
          dtree_2.get_voting_weight())
    print("********************************END OF VOTING WEIGHT********************************")

    print()

    print("********************************START OF VALIDATION ACCURACY********************************")
    # create the ensemble
    dtree_ensemble = DtreeEnsemble()
    # add the dtrees to the ensemble
    dtree_ensemble.add_dtree_to_ensemble(dtree_1)
    dtree_ensemble.add_dtree_to_ensemble(dtree_2)

    print()
    accuracy_of_dtree_1_on_valid = dtree_1.get_accuracy(
        tree_data_dictionary["valid"])
    accuracy_of_dtree_2_on_valid = dtree_2.get_accuracy(
        tree_data_dictionary["valid"])
    accuracy_of_ensemble_on_valid = dtree_ensemble.get_accuracy(
        tree_data_dictionary["valid"])
    print("Accuracy rate of Ensemble on validation set:",
          accuracy_of_ensemble_on_valid * 100, "%")
    print("Accuracy rate of Dtree 1 on validation set:",
          accuracy_of_dtree_1_on_valid * 100, "%")
    print("Accuracy rate of Dtree 2 on validation set:",
          accuracy_of_dtree_2_on_valid * 100, "%")

    print("********************************END OF VALIDATION ACCURACY********************************")


if __name__ == "__main__":
    main()
