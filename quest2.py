# [DFS] 음료수 얼려먹기
def solve_dfs():
    # N, M 입력
    n, m = map(int, input().split())
    
    # 얼음 틀 입력 (2차원 리스트)
    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))

    # DFS 함수
    def dfs(x, y):
        # 범위를 벗어나면 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        # 아직 방문하지 않은 구멍(0)인 경우
        if graph[x][y] == 0:
            graph[x][y] = 1 # 방문 처리
            # 상하좌우 재귀 호출
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    # 모든 위치에 대하여 음료수 채우기
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
                
    print(result)

# 실행
if __name__ == "__main__":
    solve_dfs()