def findCenter(edges):
    nodes = set()
    
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
    
    n = len(nodes) + 1
    
    for i in nodes:
        if len(nodes) == n - 1:
            return i
