"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  ## madeLink({}, 1, 2)
  ## if the node is not already in the graph
  ## give it an empty line
  if node1 not in G:
    G[node1] = {}

  ## always fill in the place in the graph
  ## where node1 and node2 meet
  (G[node1])[node2] = 1
  ## {1: {2:1}}
  ## at node 1, it has one linke with node 2
  
  if node2 not in G:
    G[node2] = {}
  
  (G[node2])[node1] = 1
  
  return G 


# Ring Network
ring = {} # empty graph 

n = 10 # number of nodes 

# Add in edges
rows = {} 
nodes_long = 3

## top row
for i in range(1, nodes_long):
  rows = makeLink(rows, i, (i+1)%n)
  rows = makeLink(rows, i, i+nodes_long)
  rows = makeLink(rows, i+1, i+nodes_long+1)

  ## middle row
  for i in range(1+nodes_long, nodes_long*2):
    rows= makeLink(rows, i, (i+1)%n)
    rows = makeLink(rows, i, i+nodes_long)
    rows = makeLink(rows, i+1, i+nodes_long+1)

    ## bottom row
    for i in range(1+(nodes_long*2), nodes_long*3):
      rows= makeLink(rows, i, (i+1)%n)



# Add in edges
rows = {} 
nodes_long = 4


for i in range(1, nodes_long):
  rows = makeLink(rows, i, (i+1)%n)
  rows = makeLink(rows, i, i+nodes_long)
  rows = makeLink(rows, i+1, i+nodes_long+1)

for j in range(1,1):
  for i in range(j+nodes_long*j, nodes_long*(j+1)):
    rows = makeLink(rows, i, (i+1)%n)
    rows = makeLink(rows, i, i+nodes_long)
    rows = makeLink(rows, i+1, i+nodes_long+1)


for i in range(1+(nodes_long*2), nodes_long*3):
  rows= makeLink(rows, i, (i+1)%n)













# How many nodes?
print len(ring)


# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# 16 x 16 = 256 nodes
# 
# TODO: define a function countEdges


