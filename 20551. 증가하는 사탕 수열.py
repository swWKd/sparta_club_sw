T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    cnt = 0 #감소시킨 총 횟수를 저장
    answer = 0 #최종답
    possible = True   #조건 가능 여부(상자에 사탕이 1보다 작아지면 안될 경우가 있기 때문)

    #먼저 B와 C를 확인
    # B< C 되어야 하는 상황
    if B >= C:  #B가 C보다 크거나 같다면
        old_B = B   #원래 B 값 저장
        B = C -1    #B를 C-1로 줄임(최대로 유지하면서 조건 만족)
        cnt += (old_B - B) #줄인 만큼 카운트에  더함

        #줄인 결과 B가 1보다 작아지면
        #자연수 조건을 만족 못함 -> 불가능
        if B < 1:
            possible = False



    # A와 B확인
    # A < B가 되어야 하는 상황
    if A >= B:      #만약에 A가 B보다 크거나 같다면
        old_A = A   #원래 A 값 저장
        A = B - 1   #A를 B-1로 줄임
        cnt += (old_A - A) #줄인 만큼 카운트에 더함

        # 만약에 A가 1보다 작으면
        #자연수 조건을 만족 못함 -> 불가능
        if A < 1:
            possible = False


    #조건을 다 충족했다면
    #answer에 cnt 출력하기!(감소시킨 총 횟수)
    if possible:
        answer = cnt
    #사탕을 먹어치워서 조건을 만족시킬 수 없다면 -1 출력
    else:
        answer = -1

    print(f"#{tc} {answer}")