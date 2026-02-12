T = int(input())
for tc in range(1, T+1):
    tc_num = int(input())   #테스트케이스 번호
    score = list(map(int, input().split())) # 점수 한줄을 받기

    # 학생들의 점수들을 키값으로 정하고 몇 개씩 있는지 value 값으로 넣어서
    # 최빈값을 확인하기 위함
    dict = {}

    #점수들을 우선 하나씩 뽑아서
    #딕셔너리에 그 점수의 키 값을 넣을 것임
    #딕셔너리에 우선 없으면 키 값에 1개를 넣음!
    for i in score:
        if i not in dict:
            dict[i] = 1
        # 딕셔너리에 이미 그 점수가 있으면
        # 키 값만 한 개씩 추가
        else:
            dict[i] += 1

    # 최빈 값을 구하기 위해서
    # 우선 maxv라는 변수에 0을 넣어서 비교를 할 것임
    # maxv는 value 값 즉, 그 키 값에 몇 개가 있는지!
    maxv = 0

    # 딕셔너리에 있는 키 값을 뽑아서
    # 만약 maxv(0)개 보다 많은 value가 있다면
    # 그걸로 재할당
    # 그리고 그 키 값을 일단 변수로 지정해두어야 함
    for j in dict:
        if maxv < dict[j]:
            maxv = dict[j]
            d = j

        # 문제에서
        # 단, 최빈수가 여러 개 일때에는 가장 큰 점수를 출력 해야하므로
        # maxv갯수랑 같은 value가 있다면
        # 키 값(점수)를 비교해서 가장 큰 점수가 출력 될 수 있도록 조건문
        #(아래에 if문을 하나 더 써야한다는 뜻임!!)
        elif maxv == dict[j]:
            if d < j:
                d = j

    print(f"#{tc} {d}")