from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):

		visited[v] = True
		print v,

		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	def DFS(self, v):
		visited = [False]*(len(self.graph))
		self.DFSUtil(v, visited)


g = Graph()
g.addEdg(0, 1)
g.addEdg(0, 2)
g.addEdg(1, 2)
g.addEdg(2, 0)
g.addEdg(2, 3)
g.addEdg(3, 3)

g.DFS(2)