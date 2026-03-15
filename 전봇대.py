T= int(input())
for tc in range(1, T+1):
    #전선의 갯수
    N =int(input())

    lst = []
    answer = 0

    #N개의 줄에 걸쳐 start, end = 시작점 높이, 도착점 높이가 주어짐
    for _ in range(N):
        start, end = map(int, input().split())

        #교차하기 위해선
        # 일단 이전 지점들의 시작점, 도착점을 저장해두고
        # 새로 들어오는 시작점과 도착점을 하나하나 다 비교해봐야한다

        for prev_start, prev_end in lst:
            # 1. 시작점이 이전보다 높고 도착점이 이전보다 낮은 경우
            if start > prev_start and end < prev_end:
                answer += 1
            # 2. 시작점이 이전보다 낮고 도착점이 이전보다 높은 경우
            if start < prev_start and end > prev_end:
                answer += 1
        #기존 목록에서 start, end 추가
        lst.append((start, end))

    print(f"#{tc} {answer}")