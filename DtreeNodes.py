class leafNode:
	"""leafNode description"""

	def __init__(self, label):
		self.label = label
		self.attribute = ""
		self.children = {}

	def getLabel(self):
		return self.label

class questionNode:
	"""questionNode description"""

	def __init__(self, attribute_data, most_common_label):
		self.best_attribute_data = attribute_data
		self.attribute = attribute_data[0]
		self.children = {}
		self.most_common_label_from_dataset = most_common_label

	def addChild(self, value, childNode):
		self.children[value] = childNode

	def getChild(self, value):
		return self.children[value]

	def getChildren(self):
		return self.children

	def getAttribute(self):
		return self.attribute

	def print_attribute_data(self, columns_enum):
		print("Best attribute to split on:", columns_enum(self.best_attribute_data[0]).name, "\n")
		print("Attribute value entropies:")
		for attribute_value_tuple in self.best_attribute_data[1]:
			print("H(" + columns_enum(attribute_value_tuple[0]).name, "=", attribute_value_tuple[1] + ") =",
				  self.best_attribute_data[1][attribute_value_tuple])
		print()
		print("Attribute entropies:")
		for attribute in self.best_attribute_data[2]:
			print("H(T,", columns_enum(attribute).name + ") =", self.best_attribute_data[2][attribute])
		print()
		print("Attribute information gains:")
		for attribute in self.best_attribute_data[3]:
			print("I(T,", columns_enum(attribute).name + ") =", self.best_attribute_data[3][attribute])
		print()
