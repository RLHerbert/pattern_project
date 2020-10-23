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




    """
    Build the Decision Tree. 
    """
    def build_tree(dataset): 
        list_of_subsets = []
        # find the best attribute for current data subset
        # column number
        attribute = find_best_attribute(dataset)
        
        #create question node 
        q_node = questionNode(attribute)
        # divide dataset into subsets i.e shape, fillling size 
        list_of_subsets = divide_set_by_attribute(attribute, dataset)

        for subset in list_of_subsets: 
            if DtreeMethods.__is_same_class(subset):
                # add new leafNode
                new_class = DtreeMethods.__get_class(subset[0])
                q_node.addChild(leafNode(new_class))         
            else: 
                q_node.addChild(build_tree(subset))
        return q_node




    # divide the data set by the given attribute
    # i.e attribute is shape --- return 3 subsets ! 
    # attribute is the column number 
    def divide_set_by_attribute(attribute, dataset):
        list_of_subset = []
        # list of unqiue values in the given attribute:
        unique_values = DtreeMethods.__get_unique_values_for_attribute(attribute, dataset)
        for value in unique_values:         
            subset=[]
            # for each vector in dataset  
            for example in dataset:          
                # print("example: ", example) 
                if example[attribute] == value : 
                    subset.append(example)
                   
            # list_of_subset.append((value, subset))
            list_of_subset.append(subset)
      
        return list_of_subset



    # return true if all vectors in the subset have the same class
    @staticmethod
    def __is_same_class(subset):
        num_columns = len(subset[0])
        this_class = subset[0][num_columns - 1]
        for i in range(1, len(subset)):
            if subset[i][num_columns - 1] != this_class:
               return False           
        return True
            
            
    # return subsets of each attribute 
    # shape: return cirlce, square, triangle   
    @staticmethod
    def __get_unique_values_for_attribute(attribute, dataset):
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
    def __get_class(data):
        return data[7]


