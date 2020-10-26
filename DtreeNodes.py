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

	def __init__(self, attribute):
		self.attribute = attribute
		self.children = {}

	def addChild(self, value, childNode):
		self.children[value] = childNode

	def getChild(self, value):
		return self.children[value]

	def getAttribute(self):
		return self.attribute
