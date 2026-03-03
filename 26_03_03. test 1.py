T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #2차원 배열을 받음
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우에 벽을 만날 때까지 감시를 함
    # 좌, 하, 우, 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 현재 위치를 일단 0,0
    si, sj  = 0, 0
    #2차원 배열을 돌면서
    # 만약에 현재의 값이 2라면
    #  si, sj = i, j로
    # 현재 위치를 저장함
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

                # 현재 위치에서 4방향 봐야함
                for d in range(4):
                    #이때 현재 위치를 빼고 1부터 N까지
                    for k in range(1, N):
                        #여기서 k를 곱하는 이유는
                        # 벽을 만나지 않는 한 쭉 뻗어나가기 때문
                        # k를 곱하지 않는 문제들은 상하좌우 한 칸씩만 보는거
                        ni = i + di[d] * k
                        nj = j + dj[d] * k
                        #ni, nj가 격자 안에 있고
                            # 배열이 0이 아니라면(벽이라면)
                                #break
                            # 그게 아니라면(배열의 값이 0이라면)
                                #임의의 숫자 3으로 지정
                        if 0<= ni<N and 0<= nj<N:
                            if arr[ni][nj] != 0:
                                break
                            else:
                                arr[ni][nj] =3


    # 이제는 벽을 만나는 구간을 빼고
    # 안전한 지대의 갯수를 세어야 함
    # 우선 cnt = 0이라고 지정(안전 지대 갯수 세기 위함)
    # 이차원 배열을 돌면서
    # 그 값이 0이라면
    # cnt += 1
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                cnt += 1
    print(f"#{tc} {cnt}")
