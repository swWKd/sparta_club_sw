T =int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    #M개에 줄에 걸쳐i, j가 주어진다함.
    #M = 4이면 i, j가 4번 나옴 그래서 반복문 만들기
    for _ in range(M):
        i, j = map(int, input().split())

        # 문제에서 보면 arr은 인덱스 0번부터 시작하지만
        # 색깔 바꾸는건 1번 부터 시작하기 때문에 i-1
        color = arr[i-1]
        start = i -1
        # 끝의 경우에는 i, j가 2일 때
        # end 2-1 +2 =3이 된다.
        end = i -1 + j

        # 뒤집기는 가능한 돌에 대해서만 진행
        # 예시에서 11번째가 없으면 두개만 뒤집기를 해야하니
        # end가 N보다 크거나 같으면 end는 N -1이라고 지정

        if end >= N:
            end = N-1

        #뒤집는 순회 만들기
        for A in range(start, end):
            arr[A] = color

    #arr은 리스트로 나오는데 출력은 리스트가 아니니 *를 통해 언패킹
    print(f"#{tc}", *arr)