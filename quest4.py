# [정렬] 두 배열의 원소 교체
def solve_sort():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort() # 배열 A는 오름차순 정렬
    b.sort(reverse=True) # 배열 B는 내림차순 정렬

    # 첫 번째 인덱스부터 확인하며 두 배열의 원소 교체
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break # 더 이상 교체할 필요가 없으면 탈출

    print(sum(a))

if __name__ == "__main__":
    solve_sort()