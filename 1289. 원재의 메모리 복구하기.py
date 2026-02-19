T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input()))
    # 초기값의 모든 bit가 0이라고만 문제에서 제시
    # 그 bit0의 개수는 원래값(arr)과 같아야하므로
    # 먼저 arr 리스트의 길이를 파악
    N =len(arr)

    #초기 값 bit 생성
    start = [0] * N

    #최소 수정 횟수 (한 번도 수정 안하는 0으로 일단 설정)
    cnt = 0
    for i in range(N):
        # 만약 arr[i] 값이 start[i]와 다르고 start[i]의 값이 1이라면
        # 즉, 원래 값과 초기값이 다르고 초기값 번호가 1이라면
            # cnt 횟수를 한 번 추가 하고
                #i번째 인덱스부터 끝까지 초기값의 문자를 0으로 수정
        if arr[i] != start[i] and start[i] ==1:
            cnt += 1
            for j in range(i, N):   # i인덱스부터 끝까지 문자가 수정되니 범위는 (i, N)
                start[j] = 0

        # 만약 arr[i] 값이 start[i]와 다르고 start[i]의 값이 0이라면
        # 즉, 원래 값과 초기값이 다르고 초기값 번호가 0이라면
            # cnt 횟수를 한 번 추가 하고
            # i번째 인덱스부터 끝까지 초기값의 문자를 1로 수정
        elif arr[i] != start[i] and start[i] == 0:
            cnt += 1
            for j in range(i, N):   # i인덱스부터 끝까지 문자가 수정되니 범위는 (i, N)
                start[j] = 1


    print(f"#{tc} {cnt}")