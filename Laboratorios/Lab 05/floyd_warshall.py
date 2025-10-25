from graph import GraphLink
import math

def floyd_warshall (g: GraphLink):
    n = len(g.vertices)

    if n == 0:
        return None, None, None
    
    index = {v.data: i for i, v in enumerate(g.vertices)}
    dist  = [[float('inf')]*n for _ in range(n)]
    next = [[None] * n for _ in range(n)]

