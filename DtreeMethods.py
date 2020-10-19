import math


class DtreeMethods:

    @staticmethod
    def find_best_attribute(dataset):
        num_columns = len(dataset[0])
        list_of_pi = []
        set_of_classes = set()
        # get all the possible classes
        for example in dataset:
            set_of_classes.add(example[num_columns - 1])
        for c in set_of_classes:
            list_of_pi.append(DtreeMethods.__get_pi(dataset, num_columns - 1, c, c))

        h_t = DtreeMethods.__calc_entropy(list_of_pi)

        # H(T, attribute) values
        h_t_attributes = {}
        collection_of_attribute_value_entropies = {}

        # calculate the H(T, attribute)
        for column in range(1, len(dataset[0]) - 1):
            # H(attribute = value) values
            h_attributes_values = {}

            # get possible values from column
            possible_values = set()
            for example in dataset:
                possible_values.add(example[column])
            # calculate the H(attribute = value) for each possible value
            for value in possible_values:
                list_of_pi = []
                for c in set_of_classes:
                    list_of_pi.append(DtreeMethods.__get_pi(dataset, column, value, c))
                entropy = DtreeMethods.__calc_entropy(list_of_pi)

                h_attributes_values[value] = entropy
                collection_of_attribute_value_entropies[(column, value)] = entropy

            # calculate average entropy
            average_entropy = 0
            for value in possible_values:
                average_entropy += DtreeMethods.__get_relative_freq(dataset, column, value) * h_attributes_values[value]
            h_t_attributes[column] = average_entropy

        # find attribute with most info gain
        highest_gain = 0
        best_attribute = ""
        attribute_info_gains = {}
        for attribute in h_t_attributes:
            current_gain = h_t - h_t_attributes[attribute]
            attribute_info_gains[attribute] = current_gain
            if current_gain > highest_gain:
                highest_gain = current_gain
                best_attribute = attribute

        # returns selected attribute, attribute value entropies, attribute entropies, and attribute info gains
        return best_attribute, collection_of_attribute_value_entropies, h_t_attributes, attribute_info_gains

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
    def __calc_entropy(list_of_pi):
        entropy = 0
        for pi in list_of_pi:
            if pi == 0:
                entropy += 0
            else:
                entropy += -pi * math.log2(pi)
        return entropy

    @staticmethod
    def __get_pi(dataset, attribute, value, label):
        num_examples_with_value = 0
        num_examples_with_value_with_label = 0
        num_total_examples = 0
        num_columns = len(dataset[0])

        # find number of examples with the value of a given attribute
        for example in dataset:
            num_total_examples += 1
            if example[attribute] == value:
                num_examples_with_value += 1

                if example[num_columns - 1] == label:
                    num_examples_with_value_with_label += 1

        if num_examples_with_value == 0:
            return 0

        if attribute == num_columns - 1:
            return num_examples_with_value / num_total_examples

        return num_examples_with_value_with_label / num_examples_with_value
