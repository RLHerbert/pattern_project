import random


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
