class LinkedList(object):

	def __init__(self, value):
		self.head_node = Node(value)

	## All of the 'add node' functions call the
	## 'addNodeAfter' function in different ways.

	# Function creates a Node object with 'value' as what was passed
	# in the function, and 'next_node' as the 'after_node' parameter's
	# 'next_node'. Also updates the 'after_node' 'next_node' value.
	def addNodeAfter(self, new_value, after_node):
		new_node = Node(new_value, after_node.next_node)
		after_node.next_node = new_node
		return new_node

	# Function searches for the end of the list and calls
	# 'addNodeAfter()' using that node.
	def addNode(self, new_value):
		new_node = Node(new_value)
		n = self.head_node
		while n.next_node != None:
			n = n.next_node
		n.next_node
		return self.addNodeAfter(new_value, n)

	# Function returns the Node object created during initialization.
	def headNode(self):
		return self.head_node

	# Function searches until the 'next_node' value of the Node
	# equals the specified 'before_node', then calls 'addNodeAfter()'
	# using that Node.
	def addNodeBefore(self, new_value, before_node):
		n = self.head_node
		while n.next_node != before_node:
			n = n.next_node
		return self.addNodeAfter(new_value, n)

	# Function searches through the 'next_node' variables of Nodes
	# and replaces the Nod'es 'next_node' variable when it finds
	# that the Node you're removing points to.	
	def removeNode(self, node_to_remove):
		n = self.head_node
		while n.next_node != node_to_remove:
			n = n.next_node
		n.next_node = node_to_remove.next_node

	# Function calls 'removeNode()' when it finds a Node with
	# a value equal to the parameter 'value'
	def removeNodesByValue(self, value):
		n = self.head_node
		while n.next_node != None:
			if n.value == value:
				self.removeNode(n)
			n = n.next_node
		if n.value == value:
			self.removeNode(n)

	# Helper function used in 'reverse()'.  Recursively
	# changes the node to which each node points.
	def search(self, x):
		n = self.head_node
		if x == n:
			n.next_node = None
			return None
		while n.next_node != x:
			n = n.next_node
		x.next_node = n
		return self.search(n)

	# Function moves to the end of the list, calls search()
	# to reverse all Nodes, and then changes the 'head_node'
	# as the final step.
	def reverse(self):
		n = self.head_node
		while n.next_node != None:
			n = n.next_node
		self.search(n)
		self.head_node = n

	# Function moves through the list, counting how many moves 
	# it makes before it hits a None 'next_node' value.
	def length(self):
		out = 1
		n = self.head_node
		while n.next_node != None:
			out += 1
			n = n.next_node
		return out

	# Function moves through the list, concatenating a string
	# of Node values to print.
	def __str__(self):
		print_list = ""
		n = self.head_node
		while n.next_node != None:
			print_list += str(n.value)
			print_list += ", "
			n = n.next_node
		print_list += str(n.value)
		return print_list



class Node(object):

	def __init__(self, value = None, next_node = None):
		self.value = value
		self.next_node = next_node

	def __str__(self):
		return str(self.value)




## Initializing the list.
l = LinkedList(1)
print "\nList's head node is 1"
print l

## Using 'headNode' function so I can refer
## to this node in function calls
head_node = l.headNode()

## addNode() - complexity 'n'
node_2 = l.addNode(2)
node_3 = l.addNode(3)
print "\nAdded 2, 3"
print l #1, 2, 3

## addNodeAfter() - complexity 'n'
node_7 = l.addNodeAfter(7, node_2)
print "\nAdded 7 after 2"
print l #1, 2, 7, 3

## addNodeBefore() - complexity 'n'
node_1a = l.addNodeBefore(1, node_2)
node_1b = l.addNodeBefore(1, node_1a)
node_5a = l.addNodeBefore(5, node_2)
node_5b = l.addNodeBefore(5, node_7)
print "\nAdded 1 before 2; 1 before 1; 5 before 2; and 5 before 7"
print l #1, 1, 1, 5, 2, 5, 7, 3

## removeNode() - complexity 'n'
l.removeNode(node_2)
print "\nRemoved 2"
print l #1, 1, 1, 5, 5, 7, 3

## removeNodesByValue() - complexity 'n^2'
l.removeNodesByValue(5)
print "\nRemoved all 5's"
print l ##1, 1, 1, 7, 3

## reverse() - complexity 'n!' (not positive about this one)
l.reverse()
print "\nReversed list"
print l #3, 7, 1, 1, 1



