# [이진탐색] 떡볶이 떡 만들기
def solve_binary_search():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    start = 0
    end = max(array)

    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                total += x - mid
        
        # 떡의 양이 부족한 경우 더 많이 자르기 위해 왼쪽 부분 탐색
        if total < m:
            end = mid - 1
        # 떡의 양이 충분한 경우 덜 자르기 위해 오른쪽 부분 탐색
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기서 기록
            start = mid + 1
            
    print(result)

if __name__ == "__main__":
    solve_binary_search()