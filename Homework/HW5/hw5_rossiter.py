class LinkedList(object):
	def __init__(self, value):
		self.head_node = Node(value)
	def addNode(self, new_value):
		new_node = Node(new_value)
		self.head_node.next_node = new_node
		return new_node
	def headNode(self):
		return self.head_node
	def addNodeAfter(self, new_value, after_node):
		new_node = Node(new_value, after_node.next_node)
		after_node.next_node = new_node
		return new_node, after_node
	#def addNodeBefore(self, new_value, before_node):
	#	new_node = Node(new_value)
	def length(self):
		return len(self)
	def __str__(self):
		print_list = ""
		n = self.head_node
		while n.next_node != None:
			print_list += str(n.value)
			print_list += " "
			n = n.next_node
		print_list += str(n.value)
		return print_list



class Node(object):
	def __init__(self, value = None, next_node = None):
		self.value = value
		self.next_node = next_node
	def __str__(self):
		return str(self.value)




## initializing the list
l = LinkedList(1)
head_node = l.headNode()
node_2 = l.addNode(2)
node_3 = l.addNodeAfter(3, node_2)



