"""Data Structures
Working with Graphs/Networks"""

def makeLink(G, node1, node2):
  if node1 not in G:
    G[node1] = {}
  (G[node1])[node2] = 1
  if node2 not in G:
    G[node2] = {}
  (G[node2])[node1] = 1
  return G 

# Ring Network
ring = {} # empty graph 

n = 5 # number of nodes 

# Add in edges
for i in range(n):
  ring = makeLink(ring, i, (i+1)%n)

# How many nodes?
print len(ring)

# How many edges?
print sum([len(ring[node]) for node in ring.keys()])/2 


# Grid Network
# TODO: create a square graph with 256 nodes and count the edges 
# TODO: define a function countEdges


# Social Network
class Actor(object):
  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return self.name 

  def __str__(self):
    return self.name

ss = Actor("Susan Sarandon")
jr = Actor("Julia Roberts")
kb = Actor("Kevin Bacon")
ah = Actor("Anne Hathaway")
rd = Actor("Robert DiNero")
ms = Actor("Meryl Streep")
dh = Actor("Dustin Hoffman")

movies = {}

movies = makeLink(movies, dh, rd) # Wag the Dog
movies = makeLink(movies, rd, ms) # Marvin's Room
movies = makeLink(movies, dh, ss) # Midnight Mile
movies = makeLink(movies, dh, jr) # Hook
movies = makeLink(movies, dh, kb) # Sleepers
movies = makeLink(movies, ss, jr) # Stepmom
movies = makeLink(movies, kb, jr) # Flatliners
movies = makeLink(movies, kb, ms) # The River Wild
movies = makeLink(movies, ah, ms) # Devil Wears Prada
movies = makeLink(movies, ah, jr) # Valentine's Day

# How many nodes in movies?
# How many edges in movies?

def tour(graph, nodes):
  for i in range(len(nodes)):
    print i
    node = nodes[i] 
    if node in graph.keys():
      print node 
      if i == (len(nodes) - 1):
        print "You've found an Eulerian tour!"
    else:
      print "Node not found!"
      break 
    if i+1 < len(nodes):
      next_node = nodes[i+1]
      if next_node in graph.keys():
        if next_node in graph[node].keys():
          pass 
        else:
          print "Can't get there from here!"
          break 

# TODO: find an Eulerian tour of the movie network and check it 
movie_tour = [ss, dh, rd, ms, ah, jr, kb]
tour(movies, movie_tour)


def findPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        ## for all the nodes its connected to...
        for node in graph[start]:
            ## if the node isn't ALREADY in the path...
            if node not in path:
                ## recursively call the function
                ## with the node being the new start value
                newpath = findPath(graph, node, end, path)
                if newpath:
                  return newpath
        return None

print findPath(movies, jr, ms)


# TODO: implement findShortestPath()


def findShortestPath(graph, start, end):
  paths = []
  for first_node in graph[start]:
    paths.append(findPath(graph, first_node, end))
  for p in paths:
    if len(graph[p[1]]) == 1:
      paths.append(find)





# print findShortestPath(movies, ms, ss)

# TODO: implement findAllPaths() to find all paths between two nodes

def findAllPaths(graph, start, end):
  paths = []
  for n in graph[start]:
    current_path = [start]
    append_this = findPath(graph, n, end)
    current_path.append(append_this[0])
    paths.append(current_path)
  for p in paths[0]:
    last_node = p.pop()
    for n in graph[last_node]:
      current_path = p
      append_this = findPath(graph, n, end)
      current_path.append(append_this[0])
      paths.append(current_path)
  return paths



paths = []
paths = findAllPaths(movies, jr, ms, paths)
for p in paths:
  print p
  print " "


def findAllPaths(graph, start, end, paths):
    paths = []
    actors = graph.keys()
    for n in graph[start]:
      current_path = [start]
      if n not in actors:
        continue
      else:
        current_path.append(n)
        paths.append(current_path)


    return paths



from copy import deepcopy







 

allPaths = findAllPaths(movies, jr, ms)
for path in allPaths:
   print path

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.