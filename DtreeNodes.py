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

	def __init__(self, attribute_data):
		self.best_attribute_data = attribute_data
		self.attribute = attribute_data[0]
		self.children = {}

	def addChild(self, value, childNode):
		self.children[value] = childNode

	def getChild(self, value):
		return self.children[value]

	def getAttribute(self):
		return self.attribute

	def print_attribute_data(self, columns_enum):
		print("best attribute to split on:", columns_enum(self.best_attribute_data[0]).name, "column:",
			  self.best_attribute_data[0], "\n")
		print("attribute value entropies:")
		for attribute_value_tuple in self.best_attribute_data[1]:
			print(columns_enum(attribute_value_tuple[0]).name, attribute_value_tuple[1],
				  self.best_attribute_data[1][attribute_value_tuple])
		print()
		print("attribute entropies:")
		for attribute in self.best_attribute_data[2]:
			print(columns_enum(attribute).name, self.best_attribute_data[2][attribute])
		print()
		print("attribute information gains:")
		for attribute in self.best_attribute_data[3]:
			print(columns_enum(attribute).name, self.best_attribute_data[3][attribute])
		print()
