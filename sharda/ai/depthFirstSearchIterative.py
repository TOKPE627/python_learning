# Python program to implemente Iterative Deepening Depth First Search Algorithm
#@Author TOKPE Kossi
#@Date 25 April 2021
#Student at School of Technology and Engineering
#Student Id 2020801137
#Sharda University

graph={
    'A': ['B','C'],
    'B': ['D','E'],
    "C": ['G'],
    'D': [],
    'E': ['F'],
    'G': [],
    'F': []
}
def DFS(currentNode, destination, graph, maxDepth):
    print("Checking for destination", currentNode)
    if currentNode==destination:
        return True
    if maxDepth<=0:
        return False
    for node in graph[currentNode]:
        if DFS(node, destination, graph, maxDepth-1):
            return True
    return False

def iterativeDDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        if DFS(currentNode, destination, graph, i):
            return True
    return False

if not iterativeDDFS('A','E', graph,4):
    print("Path is not available")
else:
    print("A path exists")