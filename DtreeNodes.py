class leafNode:
	"""leafNode description"""

	def __init__(self, classification):
		self.classification = classification
		self.attribute = ""
		self.children = {}

	def getClassification():
		return self.classification

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
