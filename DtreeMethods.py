import math
from Columns import Columns


class DtreeMethods:

    @staticmethod
    def find_best_attribute(dataset):
        # calc H(T) where T is the dataset
        p_pos = DtreeMethods.__get_Ppos(dataset, Columns.CLASS.value, "pos")
        print("pPos of whole set =", p_pos)
        p_neg = DtreeMethods.__get_Pneg(dataset, Columns.CLASS.value, "neg")
        print("pNeg of whole set =", p_neg)
        h_t = DtreeMethods.__calc_entropy(p_pos, p_neg)
        print("H(T) =", h_t)

        # H(T, attribute) values
        h_t_attributes = {}

        # calculate the H(T, attribute)
        for column in range(0, len(dataset[0]) - 1):
            # H(attribute = value) values
            h_attributes_values = {}

            # get possible values from column
            possible_values = set()
            for example in dataset:
                possible_values.add(example[column])
            # calculate the H(attribute = value) for each possible value
            for value in possible_values:
                p_pos = DtreeMethods.__get_Ppos(dataset, column, value)
                p_neg = DtreeMethods.__get_Pneg(dataset, column, value)
                entropy = DtreeMethods.__calc_entropy(p_pos, p_neg)
                h_attributes_values[value] = entropy

            # calculate average entropy
            average_entropy = 0
            for value in possible_values:
                average_entropy += DtreeMethods.__get_relative_freq(dataset, column, value) * h_attributes_values[value]
            h_t_attributes[Columns(column).name] = average_entropy

        for attribute in h_t_attributes:
            print(attribute, h_t_attributes[attribute])

        # find attribute with most info gain
        highest_gain = 0
        best_attribute = ""
        for attribute in h_t_attributes:
            current_gain = h_t - h_t_attributes[attribute]
            if current_gain > highest_gain:
                highest_gain = current_gain
                best_attribute = attribute

        return best_attribute

    @staticmethod
    def __get_relative_freq(dataset, attribute, value):
        num_total_examples = 0
        num_examples_with_value = 0
        for example in dataset:
            num_total_examples += 1
            if example[attribute] == value:
                num_examples_with_value += 1

        if num_total_examples == 0:
            return 0
        return num_examples_with_value / num_total_examples

    @staticmethod
    def __calc_entropy(p_pos, p_neg):
        if p_pos == 0 or p_neg == 0:
            return 0
        return -p_pos * math.log2(p_pos) - p_neg * math.log2(p_neg)

    @staticmethod
    def __get_Ppos(dataset, attribute, value):
        num_examples_with_value = 0
        num_pos_examples_with_value = 0
        num_total_examples = 0

        # find number of examples with the value of a given attribute
        for example in dataset:
            num_total_examples += 1
            if example[attribute] == value:
                num_examples_with_value += 1

                # check to see if it is positive
                if example[Columns.CLASS.value] == "pos":
                    num_pos_examples_with_value += 1

        if num_examples_with_value == 0:
            return 0

        if attribute == Columns.CLASS.value:
            return num_examples_with_value / num_total_examples

        return num_pos_examples_with_value / num_examples_with_value



    @staticmethod
    def __get_Pneg(dataset, attribute, value):
        num_examples_with_value = 0
        num_neg_examples_with_value = 0
        num_total_examples = 0

        # find number of examples with the value of a given attribute
        for example in dataset:
            num_total_examples += 1
            if example[attribute] == value:
                num_examples_with_value += 1

                # check to see if it is positive
                if example[Columns.CLASS.value] == "neg":
                    num_neg_examples_with_value += 1

        if num_examples_with_value == 0:
            return 0

        if attribute == Columns.CLASS.value:
            return num_examples_with_value / num_total_examples

        return num_neg_examples_with_value / num_examples_with_value
