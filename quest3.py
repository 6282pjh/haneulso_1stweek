# 미로 탈출 코드
from collections import deque
n, m = map(int, input().split()) # N, M 입력
graph = [list(map(int, list(input()))) for _ in range(n)]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우 확인
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0: continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]
print(bfs(0, 0))