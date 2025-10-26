from graph import GraphLink

def floyd_warshall (g: GraphLink):
    n = len(g.vertices)
    
    if n == 0:
        return []
    
    index = {v.data: i for i, v in enumerate(g.vertices)}
    dist  = [[float('inf')] * n for _ in range(n)]
    