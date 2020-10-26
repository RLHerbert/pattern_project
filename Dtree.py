import math
from DtreeNodes import leafNode
from DtreeNodes import questionNode
import random


class Dtree:
    def __init__(self, dataset, columns_enum):
        self.__root = self.__build_tree(dataset)
        self.__columns_enum = columns_enum
        self.__list_possible_labels = self.__get_possible_labels_from_data(dataset)

    # wrapper method
    def getClassification(self, example):
        return self.__getClassification(self.__root, example)

    def output_q_node_data(self):
        return self.__output_q_node_data(self.__root)

    # THE REST OF THE STUFF BELOW ARE PRIVATE METHODS****************

    # recursive method for finding classification
    def __getClassification(self, node, example):
        if isinstance(node, leafNode):
            return node.getLabel()
        elif isinstance(node, questionNode):
            attribute = node.getAttribute()
            value = example[attribute]
            # need to check for missing edge
            if value in node.children:
                return self.__getClassification(node.getChild(value), example)
            else:
                # we have a missing edge, need to give a random class
                random_index = random.randint(0, len(self.__list_possible_labels) - 1)
                return self.__list_possible_labels[random_index]

    def __output_q_node_data(self, node):
        if isinstance(node, leafNode):
            return
        elif isinstance(node, questionNode):
            #print the q node data
            print("***************************QUESTION NODE ATTRIBUTE DATA***************************")
            node.print_attribute_data(self.__columns_enum)
            for value in node.children:
                self.__output_q_node_data(node.getChild(value))



    def __get_possible_labels_from_data(self, dataset):
        set_of_possible_classes = set()
        num_columns = len(dataset[0])
        for example in dataset:
            set_of_possible_classes.add(example[num_columns - 1])
        return list(set_of_possible_classes)

    def __find_best_attribute(self, dataset):
        num_columns = len(dataset[0])
        list_of_pi = []
        set_of_classes = set()
        # get all the possible classes
        for example in dataset:
            set_of_classes.add(example[num_columns - 1])
        for c in set_of_classes:
            list_of_pi.append(self.__get_pi(dataset, num_columns - 1, c, c))

        h_t = self.__calc_entropy(list_of_pi)

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
                    list_of_pi.append(self.__get_pi(dataset, column, value, c))
                entropy = self.__calc_entropy(list_of_pi)

                h_attributes_values[value] = entropy
                collection_of_attribute_value_entropies[(column, value)] = entropy

            # calculate average entropy
            average_entropy = 0
            for value in possible_values:
                average_entropy += self.__get_relative_freq(dataset, column, value) * h_attributes_values[value]
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

        # case of no best attribute to split on. this means we will have a leaf
        if best_attribute == "":
            best_attribute = -1
        # returns selected attribute, attribute value entropies, attribute entropies, and attribute info gains
        return best_attribute, collection_of_attribute_value_entropies, h_t_attributes, attribute_info_gains

    def __get_relative_freq(self, dataset, attribute, value):
        num_total_examples = 0
        num_examples_with_value = 0
        for example in dataset:
            num_total_examples += 1
            if example[attribute] == value:
                num_examples_with_value += 1

        if num_total_examples == 0:
            return 0
        return num_examples_with_value / num_total_examples

    def __calc_entropy(self, list_of_pi):
        entropy = 0
        for pi in list_of_pi:
            if pi == 0:
                entropy += 0
            else:
                entropy += -pi * math.log2(pi)
        return entropy

    def __get_pi(self, dataset, attribute, value, label):
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

    """
        Build the Decision Tree. 
    """

    # return best_attribute, collection_of_attribute_value_entropies, h_t_attributes, attribute_info_gains
    def __build_tree(self, dataset):
        list_of_subsets = []
        # find the best attribute for current data subset
        best_attribute_data = self.__find_best_attribute(dataset)

        # create question node using the best attribute
        q_node = questionNode(best_attribute_data)
        # divide dataset into subsets i.e shape, fillling size
        list_of_subsets = self.__divide_set_by_attribute(best_attribute_data[0], dataset)

        for subset in list_of_subsets:
            if self.__is_same_class(subset[1]):
                # add new leafNode
                new_class = self.__get_class(subset[1][0])
                child_node = leafNode(new_class)
                # add the class with its subset
                # print("subset[1] ", subset[1])
                q_node.addChild(subset[0], child_node)
                # print("adding child  node: ", child_node.label)
                # print("its children are: ", q_node.getChild(child_node.label))
            else:
                q_node.addChild(subset[0], self.__build_tree(subset[1]))
        return q_node

    # divide the data set by the given attribute
    # i.e attribute is shape --- return 3 subsets !
    # return list of tuple (square, list_of_square_subset)...
    def __divide_set_by_attribute(self, attribute, dataset):
        list_of_subset = []
        # list of unqiue values in the given attribute:
        unique_values = self.__get_unique_values_for_attribute(attribute, dataset)
        for value in unique_values:
            subset = []
            # for each vector in dataset
            for example in dataset:
                # print("example: ", example)
                if example[attribute] == value:
                    subset.append(example)

            list_of_subset.append((value, subset))

        return list_of_subset

    # return true if all vectors in the subset have the same class
    def __is_same_class(self, subset):
        num_columns = len(subset[0])
        this_class = subset[0][num_columns - 1]
        for i in range(1, len(subset)):
            if subset[i][num_columns - 1] != this_class:
                return False
        return True

    # return subsets of each attribute
    # shape: return cirlce, square, triangle
    def __get_unique_values_for_attribute(self, attribute, dataset):
        subset = []
        for example in dataset:
            # print(example)
            # print('attribute: ', example[attribute])
            if not subset:
                subset.append(example[attribute])
            if example[attribute] not in subset:
                subset.append(example[attribute])
        # print(subset)
        return subset

    # return the class of each vector
    def __get_class(self, data):
        num_columns = len(data)
        return data[num_columns - 1]
