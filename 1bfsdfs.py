from collections import deque,defaultdict

def bfs_of_graph(adj, start_vertex):
    bfs = []
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    
    while queue:
        node = queue.popleft()
        bfs.append(node)
        for neighbour in adj[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                
    return bfs

def dfs_of_graph(adj, start_vertex):
    dfs = []
    visited = set()

    # Sort the adjacency list for consistent DFS order
    for key in adj:
        adj[key].sort()

    def dfs_util(node):
        visited.add(node)
        dfs.append(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs_util(neighbor)

    dfs_util(start_vertex)
    return dfs

def main():
    V = int(input("Enter no of vertices :"))
    E = int(input("Enter no of edges :"))
    adj = defaultdict(list)
    print("Enter the edges (source destination): ")
    for i in range (E):
        edge = input().strip().split()
        u, v = edge[0], edge[1]
        adj[u].append(v)
        adj[v].append(u)
    start_vertex = input("Enter the starting vertex: ")
    bfs_result = bfs_of_graph(adj, start_vertex)
    dfs_result = dfs_of_graph(adj, start_vertex)
    print("BFS :",bfs_result)
    print("DFS Traversal:", dfs_result)
    
if __name__ == "__main__":
    main()