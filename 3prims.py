import heapq

def prim_mst(graph, start):
    num_vertices = len(graph)
    mst = []  # To store the resulting Minimum Spanning Tree
    visited = [False] * num_vertices
    min_heap = []

    # Push the starting vertex with weight 0 and no parent (-1)
    heapq.heappush(min_heap, (0, start, -1))

    while min_heap:
        weight, u, prev = heapq.heappop(min_heap)

        if visited[u]:
            continue

        visited[u] = True

        # Add edge to MST (ignore the first dummy edge)
        if prev != -1:
            mst.append((prev, u, weight))

        # Explore all adjacent vertices
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst

def get_graph_input():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = {i: [] for i in range(num_vertices)}

    num_edges = int(input("Enter the number of edges: "))

    print("Enter the edges (start_vertex end_vertex weight):")
    for _ in range(num_edges):
        u, v, weight = map(int, input().split())
        graph[u].append((v, weight))
        graph[v].append((u, weight))  # Since the graph is undirected

    return graph

def main():
    graph = get_graph_input()
    start_vertex = int(input("Enter the starting vertex for Prim's algorithm: "))

    mst = prim_mst(graph, start_vertex)

    print("\nEdges in the Minimum Spanning Tree:")
    total_weight = 0
    for u, v, w in mst:
        print(f"{u} - {v} with weight {w}")
        total_weight += w

    print(f"\nTotal weight of MST: {total_weight}")

if __name__ == "__main__":
    main()
