T = int(input())
for tc in range(1, T+1):
    # N = 사람의 자격 수
    # M = 붕어빵 만드는 시간
    # K = 붕어빵 갯수
    N, M, K = map(int, input().split())
    #arr = 손님들의 도착 시간(초의 단위)
    # arr은 정렬이 안되어 있다
    # 예를 들면 4 3
    # 3초에 1명 4초에 2명인거임
    arr = list(map(int, input().split()))
    #따라서 일단 arr을 정렬한다
    arr.sort()

    #정답을 먼저 "Possible"로 적어두기
    # 즉 붕어빵을 모든 손님에 대해 기다리는 시간이 없이 제공할 수 있다는 뜻
    answer = "Possible"

    #지금까지 만들어진 붕어빵은
    # arr[i] // M * K임
    # 즉 손님1이 2라면
    # 2//2 = 1
    # 1 * 2 = 2
    # 손님1이 2초에 왔다면 2초만에 2개를 만들 수 있으니
    # 식이 arr[i] // M * K이다
    # 만약에 지금까지 만들어진  붕어빵이 손님의 수보다 작게 되면
    #Impossible
    for i in range(N):
        if (arr[i]//M) * K < i+1:
            answer = "Impossible"
            break
    print(f"#{tc} {answer}")