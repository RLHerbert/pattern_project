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
    # TODO: PRINT TRAINING, HOLDT, AND VALID SET FOR dtree_1 AND dtree_2

    # create the first tree
    dtree_1 = Dtree(tree_data_dictionary["train"], CHESS_COLUMNS)
    print("********************************START OF DTREE 1 CONSTRUCTION DETAILS********************************")
    dtree_1.output_everything()
    print("*********************************END OF DTREE 1 CONSTRUCTION DETAILS*********************************")

    print()

    # create the second tree
    dtree_2 = from_misclassified(tree_data_dictionary, dtree_1)
    print("**************************************START OF DTREE 2 DETAILS**************************************")
    dtree_2.output_parents()
    print("***************************************END OF DTREE 2 DETAILS***************************************")
    
    print()
    # TODO PRINT MISCLASSIFIED HOLDOUT VECTORS

    # printing accuracies based on hold out set
    accuracy_of_dtree_1_on_holdt = dtree_1.get_accuracy(tree_data_dictionary["holdt"])
    accuracy_of_dtree_2_on_holdt = dtree_2.get_accuracy(tree_data_dictionary["holdt"])
    print("Accuracy of Dtree 1 on holdout set:", accuracy_of_dtree_1_on_holdt)
    print("Accuracy of Dtree 2 on holdout set:", accuracy_of_dtree_2_on_holdt)


    # setting the voting weights as the accuracies for now
    dtree_1.set_voting_weight(accuracy_of_dtree_1_on_holdt)
    dtree_2.set_voting_weight(accuracy_of_dtree_2_on_holdt)
    print()
    print("Voting weight of Dtree 1:", dtree_1.get_voting_weight())
    print("Voting weight of Dtree 2:", dtree_2.get_voting_weight())

    # create the ensemble
    dtree_ensemble = DtreeEnsemble()
    # add the dtrees to the ensemble
    dtree_ensemble.add_dtree_to_ensemble(dtree_1)
    dtree_ensemble.add_dtree_to_ensemble(dtree_2)

    print()
    accuracy_of_dtree_1_on_valid = dtree_1.get_accuracy(tree_data_dictionary["valid"])
    accuracy_of_dtree_2_on_valid = dtree_2.get_accuracy(tree_data_dictionary["valid"])
    accuracy_of_ensemble_on_valid = dtree_ensemble.get_accuracy(tree_data_dictionary["valid"])
    print("Accuracy of Ensemble on validation set:", accuracy_of_ensemble_on_valid)
    print("Accuracy of Dtree 1 on validation set:", accuracy_of_dtree_1_on_valid)
    print("Accuracy of Dtree 2 on validation set:", accuracy_of_dtree_2_on_valid)


if __name__ == "__main__":
    main()
