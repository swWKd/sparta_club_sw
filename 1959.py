T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maxv = -10000000    # A와 B안에 음수도 있기 때문에 최댓값을 일단 엄청 작은 수로 가정

    # N이 M보다 클 수도 있고 작을 수도 있다.
    #먼저 N이 M보다 큰 경우
    if N < M:
        # 작은 배열을 큰 배열 안에서 벗어나지 않고
        # 끝까지 이동 시킬 수 있는 시작 위치
        for i in range(M - N + 1):
            # 작은 배열이 움직일 때 total 값은 리셋 되어야 하기 때문에 지정
            total = 0

            # 현재 위치에서 마주보는 원소들의 곱을 모두 더함
            # i =0 일때 j는 0, 1, 2 다돈다.(N=3, M=5라고 가정)
            # A[0] * B[0], A[1] * B[1], A[2] * B[2]
            for j in range(N):
                total += A[j] * B[i+j]

            # 가정해둔 최댓값보다 total이 크면 그걸 재할당
            # if문의 위치가 여기인 이유
            # 한 위치에서의 곱셈 합이 모두 계산된 후에
            # 최댓값과 비교해야하므로 if문이 반복문 밖으로 나옴!!!!!
            if maxv < total:
                maxv = total

    #M이 N보다 크거나 작은경우(같은 경우는 위도 아래도 상관이 없음)
    if N >= M:
        # 작은 배열을 큰 배열 안에서 벗어나지 않고
        # 끝까지 이동 시킬 수 있는 시작 위치
        for i in range(N - M + 1):
            #작은 배열이 움직일 때 total 값은 리셋 되어야 하기 때문에 지정
            total = 0

            # 현재 위치에서 마주보는 원소들의 곱을 모두 더함
            # i =0 일때 j는 0, 1, 2 다돈다.(N=3, M=5라고 가정)
            # A[0] * B[0], A[1] * B[1], A[2] * B[2]
            for j in range(M):
                total += A[i +j] * B[j]

            # 가정해둔 최댓값보다 total이 크면 그걸 재할당
            # if문의 위치가 여기인 이유
            # 한 위치에서의 곱셈 합이 모두 계산된 후에
            # 최댓값과 비교해야하므로 if문이 반복문 밖으로 나옴!!!!!
            if maxv < total:
                maxv = total

    print(f"#{tc} {maxv}")

