# Python program to implemente Breadth First Search Algorithm
#@Author TOKPE Kossi
#@Date 27 April 2021
#Student at School of Technology and Engineering
#Student Id 2020801137
#Sharda University

from queue import Queue


adj={
        'u':['v','x'],
        'x':['u','v','y'],
        'v':['u','x','y'],
        'y':['w'],
        'w':['y','z'],
        'z':['w']
    }
traversed, visited, level, parent = breadth_first_search(adj)


def breadth_first_search(adj_list):
    visited          = {}
    level            = {}
    parent           = {}
    traversal_output = []
    queue            = Queue()

    for node in adj_list.keys():
        visited[node] = False
        parent[node]  = None
        level[node]   = -1

    s="u"
    visited[s] = True
    level[s]   = 0
    queue.put(s)

    while not queue.empty():
        u=queue.get()
        traversal_output.append(u)
        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v]  = u
                level[v]   = level[u] + 1
                queue.put(v)
    return traversal_output, visited, level, parent
  