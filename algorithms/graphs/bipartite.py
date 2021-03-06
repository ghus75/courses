#Uses python3

import sys
import queue

from collections import deque

def bipartite(adj):
    #write your code here
    
    color = [-1] * len(adj)
    flag = 1
    #write your code here
    def bfs(vertex, adj):    
    # bfs algortihm
    # number of vertices
        nonlocal flag
        color[vertex] = 0
        Q = deque([vertex])
    
        while Q:
            u = Q.popleft()
            for neighbor in adj[u]:
                if color[neighbor] == -1:
                    Q.append(neighbor)
                    color[neighbor] = 1 - color[u]
                #prev[neighbor] = u
                if color[neighbor] == color[u]:
                    flag = 0 #not bipartite
                    

    
    for vertex in range(len(adj)):
        if color[vertex] == -1:
            bfs(vertex, adj)
    
    return flag

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
