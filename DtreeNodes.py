class leafNode:
	"""leafNode description"""

	def __init__(self, label):
		self.label = label
		self.attribute = ""
		self.children = {}

	def getLabel():
		return self.label

class questionNode:
	"""questionNode description"""

	def __init__(self, attribute):
		self.attribute = attribute
		self.children = {}

	def addChild(self,childNode, value):
		self.children[value] = childNode

	def getChild(self, value):
		return self.children[value]

	def getAttribute():
		return self.attribute
