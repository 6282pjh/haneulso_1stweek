INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1): graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

x, k = map(int, input().split())

for z in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][z] + graph[z][j])

dist = graph[1][k] + graph[k][x]
print(dist if dist < INF else -1)