import heapq

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = float('inf')

dist = [[INF] * (K + 1) for _ in range(N + 1)]

dist[1][0] = 0

pq = [(0, 1, 0)]

while pq:
    cost, node, edges = heapq.heappop(pq)

    if cost != dist[node][edges]:
        continue

    if node == N:
        print(cost)
        break

    if edges == K:
        continue

    for next_node, weight in graph[node]:
        new_cost = cost + weight
        new_edges = edges + 1

        if new_cost < dist[next_node][new_edges]:
            dist[next_node][new_edges] = new_cost
            heapq.heappush(pq, (new_cost, next_node, new_edges))

else:
    print(-1)