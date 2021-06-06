# Find path from one node to another using Python dict as a adjacency list.


def find_path(graph, start, end, path=[]):

    path = path + [start]

    if start == end:
        return path

    for node in graph[start]:
        if node not in path:
            path = find_path(graph, node, end, path)
            if path:
                return path


graph = {'a': ['c'], 'b': ['d'], 'c': ['e'], 'd': ['a', 'd'], 'e': ['b', 'c']}
print(find_path(graph, 'e', 'a'))
