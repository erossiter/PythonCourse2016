class LinkedList(object):
	def __init__(self, value):
		self.head_node = Node(value)
	def addNode(self, new_value):
		new_node = Node(new_value)
		self.head_node.next_node = new_node
		return new_node
	## needed to be able to have the node object created during initialization,
	## so this function returns it for a user's use
	def headNode(self):
		return self.head_node
	def addNodeAfter(self, new_value, after_node):
		new_node = Node(new_value, after_node.next_node)
		after_node.next_node = new_node
		return new_node, after_node
	def addNodeBefore(self, new_value, before_node):
		n = self.head_node
		while n.next_node != before_node:
			n = n.next_node
		self.addNodeAfter(new_value, n)
	def length(self):
		out = 1
		n = self.head_node
		while n.next_node != None:
			out += 1
			n = n.next_node
		return out
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
node_7 = l.addNodeAfter(7, node_2)
node_5 = l.addNodeBefore(5, node_2)



