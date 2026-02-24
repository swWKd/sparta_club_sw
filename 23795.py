T =int(input())
for tc in range(1, T+1):
    N =int(input())
    # 2차원배열로 나타나져 있으므로 이를 받을 땐 이렇게 사용
    arr=[list(map(int, input().split())) for _ in range(N)]

    #괴물의 위치를 기준으로 상하좌우를 dx, dy로 표현
    #즉 dx[0]은 행의 번호 dy[0]은 상의 좌표다
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    #먼저 현재위치를 알아야함
    # 문제에서 괴물이 있는 위치는 2라고 되어있음
    # 따라서 만약에 arr[i][j] == 2이면
    # 그 현 위치를 기록해둠
    # 왜냐? 상하좌우에 광선을 계속 뻗어간 걸 체킹하기 위함
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x, y = i, j


    #상하좌우 4번 돌릴거고
    #괴물 자기 위치를 제외하고 N-1까지 뻗어가므로
    # 범위는 1, N까지 표시해두기
    # 이때 새로운 ni, nj의 인덱스 번호 변수를 만들거임
    # 광선이 뻗어가는 위치를 저장하기 위해서
    # for문을 돌리게 되면
    # N이 5일 때
    # ni = x +(1 * dx[0])
    # nj = y +(1 * dy[0])
    # ni = x +(2 * dx[0])
    # nj = y +(2 * dy[0])
    # .....
    # ni = x +(N * dx[0])
    # nj = x +(N * dy[0]로 끝나는 것...
    # 그리고 다시 a가 1로 바뀌고 반복
    for a in range(4):
        for b in range(1, N):
            ni = x + (b * dx[a])
            nj = y + (b * dy[a])

            #이는 ni,nj가 N*N에 있는 범위 안에서 확인하기 위함
            if 0 <= ni < N and 0 <= nj <N:
                #이때 0이 아니라면 멈추고
                #(즉, 벽이 1이니 그땐 멈추고)
                # 0인 경우는 아무 것도 없지만 괴물에 의해 광선이 뻗어가므로
                # 1, 2가 아닌 그냥 3으로 지정
                if arr[ni][nj] != 0:
                    break
                else:
                    arr[ni][nj] =3

    #이제는 배열 중에 0인(안전지대)인 곳 갯수 세기
    # 처음엔 0개로 지정
    # 만약에 0이라면 cnt 1개씩 증가
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    print(f"#{tc} {cnt}")
