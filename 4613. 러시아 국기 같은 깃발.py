T = int(input())
for tc in range(1, T+1):
    #N개의 줄에 M개의 문자
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))

    # 새로 칠해야 하는 칸의 최솟값을 구해야함
    # 마지막에 조건문으로 비교한 후 최솟값을 지정하기 위해
    # 큰 수로 최솟값 변수를 지정
    min_total = 9999999

    # 우리는 색을 3개의 상자로 나눈다
    # W / B / R

    # 2차원 배열을 기준으로 두 군데를 자르면
    # 3개의 구간이 만들어진다

    # i는 W 상자의 마지막 위치
    # j는 B 상자의 마지막 위치

    # W : 0 ~ i
    # B : i+1 ~ j
    # R : j+1 ~ N-1

    # i는 최소 0부터 시작
    # i는 N-3까지만 가능
    for i in range(N-2):
        for j in range(i+1, N-1):
            # 카운트
            # 색을 몇 번 바꿔야 할지 셀 변수
            total = 0

            # W : 0 ~ i
            # B : i+1 ~ j
            # R : j+1 ~ N-1

            # 처음 줄
            # 즉 W여야 할 줄은 0번 인덱스부터 i까지
            # 그런데 W가 아닐 경우
            # total +=1
            for r in range(0, i+1):
                for c in range(M):
                    if arr[r][c] != "W":
                        total += 1
            # B 여야 하는 줄은 인덱스 i+1부터 j까지
            # 그런데 B가 아닐 경우
            # total +=1
            for r in range(i+1, j+1):
                for c in range(M):
                    if arr[r][c] != "B":
                        total +=1
            #R이어야 하는 줄은 인덱스 j+1부터 N-1까지
            #그런데 R이 아닐 경우
            # total +=1
            for r in range(j+1, N):
                for c in range(M):
                    if arr[r][c] != "R":
                        total+=1

            #아까 위에서 지정해둔 최소 횟수 변수를 다시 지정
            min_total = min(min_total, total)

    print(f"#{tc} {min_total}")