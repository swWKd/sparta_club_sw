T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    #M개에 줄에 걸쳐i, j가 주어진다함.
    #M = 4이면 i, j가 4번 나옴 그래서 반복문 만들기
    for _ in range(M):
        i, j = map(int, input().split())
        # 중심인덱스
        center = i -1

        for A in range(1, j+1):
            left = center - A
            right = center + A

            # 범위 벗어나면 중단
            if left < 0 or right >= N:
                break

            # 같으면 뒤집기
            if arr[left] == arr[right]:
                arr[left] = 1- arr[left]
                arr[right] = 1 - arr[right]

    print(f"#{tc}", *arr)

