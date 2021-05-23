def createGraph(graph):
    n = int(input("Enter the number of nodes in graph:-"))
    for _ in range(n):
        node = input("Enter nodes and connected nodes in following format \nnode:connectedNode1, connectedNode2,...").split(":")
        graph[node[0]] = node[1].split(",")
    return graph

def bfs(graph, start, dest):
    result    = ["Not reachable", list()]
    visited   = list()
    queue     = list()
    queue.append(start)
    visited.append(start)
    while queue:
        currentNode = queue.pop(0)
        if(currentNode not in graph.keys()):
            continue

        for node in graph[currentNode]:
            if(node not in graph.keys()):
                continue

            if(node==dest):
                result[0]="Reachable"
                break
            if(node not in visited):
                visited.append(node)
                queue.append(node)
    result[1] = visited
    return result

graph = dict()
graph = createGraph(graph)
start = input("Enter the starting point of traversal:-")
end   = input("Enter the ending point of traversal:-")
result = bfs(graph, start, end)
print("Result:-", result[0])
print("Path traversed:-", result[1])
