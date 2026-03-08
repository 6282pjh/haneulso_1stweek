def solve():
    # 1. 공간의 크기 N 입력 
    try:
        n = int(input())
        # 2. 이동 계획서 입력 
        plans = input().split()
    except EOFError:
        return

    # 3. 여행가 A의 시작 좌표는 항상 (1, 1) 
    x, y = 1, 1

    # 4. 이동 방향 정의 
    # L: 왼쪽 (y-1), R: 오른쪽 (y+1), U: 위 (x-1), D: 아래 (x+1)
    moves = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    # 5. 계획서에 따라 이동 
    for plan in plans:
        dx, dy = moves[plan]
        nx, ny = x + dx, y + dy

        # 6. 공간(N x N)을 벗어나는 움직임은 무시 
        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny

    # 7. 최종 도착 지점 좌표 출력 
    print(f"{x} {y}")

if __name__ == "__main__":
    solve()