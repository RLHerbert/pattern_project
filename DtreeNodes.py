"""
DtreeNodes.py - Class that encapsulates the leaf and question nodes and
proves functions to operate on them

Dennis La - Dennis.La@student.csulb.edu
Melissa Hazlewood - Melissa.Hazlewood@student.csulb.edu
Rowan Herbert - Rowan.Herbert@student.csulb.edu
Sophanna Ek - Sophanna.Ek@student.csulb.edu
"""
class leafNode:
	"""leafNode description"""

	def __init__(self, label):
		self.__label = label

	def get_label(self):
		return self.__label

class questionNode:
	"""questionNode description"""

	def __init__(self, attribute_data, most_common_label):
		self.__best_attribute_data = attribute_data
		self.__attribute = attribute_data[0]
		self.__children = {}
		self.most_common_label_from_dataset = most_common_label

	def add_child(self, value, child_node):
		self.__children[value] = child_node

	def get_child(self, value):
		return self.__children[value]

	def get_children(self):
		return self.__children

	def get_attribute(self):
		return self.__attribute

	def print_attribute_data(self, columns_enum):
		print("Best attribute to split on:", columns_enum(self.__best_attribute_data[0]).name, "\n")
		print("Attribute value entropies:")
		for attribute_value_tuple in self.__best_attribute_data[1]:
			print("H(" + columns_enum(attribute_value_tuple[0]).name, "=", attribute_value_tuple[1] + ") =",
				  self.__best_attribute_data[1][attribute_value_tuple])
		print()
		print("Attribute entropies:")
		for attribute in self.__best_attribute_data[2]:
			print("H(T,", columns_enum(attribute).name + ") =", self.__best_attribute_data[2][attribute])
		print()
		print("Attribute information gains:")
		for attribute in self.__best_attribute_data[3]:
			print("I(T,", columns_enum(attribute).name + ") =", self.__best_attribute_data[3][attribute])
		print()
