from queue import Queue

visited          = {}
level            = {}
parent           = {}
traversal_output = []
queue            = Queue()

adj_list={
    'u':['v','x'],
    'x':['u','v','y'],
    'v':['u','x','y'],
    'y':['w'],
    'w':['y','z'],
    'z':['w']
}

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
print("All nodes:",traversal_output)
print("Nodes visited:", visited)
print("Level of node:", level)
print("Parents of nodes:", parent)

#Short path of w
v="w"
path = []
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()

print()
print("Short path of v")

print(path)