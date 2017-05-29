"""
Common search algorithms.
"""



def breadthfirst(graph,start, end):
    """
    Inputs:
        graph : Dictionary of connecting nodes
        start : Integer starting point on the graph
        end   : Integer ending point on the graph
    Outputs:
        path  : List of shortest path
        taken : List of the nodes checked in order
    """
    queue = []
    queue.append([start])
    taken = []
    while queue:
        path = queue.pop(0)
        node = path[-1]
        taken.append(node)
        if node == end:
            return path, taken
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
