T = int(input())
for tc in range(1, T+1):
    N, K =map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    #10개의 평점을 우선 리스트에 담는다!
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    # 비율을 반영한 총점을 정렬하기 위해 빈 리스트를 만듦

    lst = []
    # 이중리스트에 과목은 3개이니 중간, 기말, 과제 인덱스는 고정
    for i in range(N):
        score = arr[i][0] * 0.35 + arr[i][1] * 0.45 + arr[i][2] * 0.20
        # 리스트에 총점을 넣기
        lst += [score]
        # i는 인덱스 번호이기 때문에
        # K의 학생의 점수를 확인하기 위해선 K-1을 해줘야함
        # 즉 K번째 학생은 인덱스 K-1임
        # 예를 들어서 K=2라고 하고 K의 오름차순으로 성적도 오름차순이라고 할 때
        # 2번째의 학생 인덱스는 1이다. 따라서 K-1라고 해야함.
        if i == K-1:
            k_score = score

    #sort 내장 함수를 못쓰니 ㅠ
    # 내림차순으로 정리할 때 버블정렬 이용해서 하기
    # 내림차순이니깐 부등호 방향이 < 됨!
    for j in range(N):
        for z in range(N-1-j):
            # 앞의 값이 더 작으면 서로 교환 → 큰 값이 앞으로 이동
            if lst[z] < lst[z+1]:
                lst[z], lst[z+1] = lst[z+1], lst[z]

    # K번째 학생의 등수(인덱스 찾기)
    for idx in range(N):
        # 총점을 담은 lst에 k번째 학생의 점수를 만나게 되면
        # 그 인덱스를 일단 rank라고 지정
        # k_score와 동일한 친구는 없으니깐(문제에서 그렇다고 함)
        # 뒤에 다른걸 더 볼 필요가 X
        if lst[idx] == k_score:
            rank = idx
            break

    # 한 grade 당 들어가는 학생의 수
    # N은 이미 10의 배수라고 했음 !
    # N= 30 일 때 한 grade 당 3명씩 들어갈 수 있으니깐 아래와 같이 적음
    size = N // 10

    # 등수 인덱스를 grade 구간 크기로 나누어서
    # 해당하는 학점을 결정함!!
    # size는 항상 10으로 나누어 떨어진 몫이기에
    # 한 비율당 들어가는 인원이고
    # 만약 한 비율당 3명이 들어가고 rank가 3일 때
    # 나누면 1 그럼 A+에 들어가게 됨!
    result = grade[rank // size]

    print(f'#{tc} {result}')
