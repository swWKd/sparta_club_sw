# a = 2의 지수
# b = 3의 지수
# c = 5의 지수
# d = 7의 지수
# e = 11의 지수
# 문제에서 a,b,c,d,e를 출력하라고 함
#(출력할 때 지수마다 공백으로 구분됨)

T = int(input())
for tc in range(1, T + 1):
    arr = int(input())
    # 소인수 분해를 하기 전에
    #우선 dict에 2, 3, 5, 7, 11의 지수들을 다 0으로 만들어놓는다.
    dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}

    #dict 안에 key를 하나씩 뽑고
    # while문으로 주어진 arr에 key(소수)들을 나눈다
    #(몇 번 반복을 해야할지 모르니 while문 사용)
    # 소인수분해를 통해 딱 나누어 떨어져야 하고
    # 나누어 떨어질 수 있도록 하는 key 값이 있으면
    # 딕셔너리에 value 값 하나 씩 추가를 한다.

    # 그러고 key로 나누었을 때의 몫을 다시 arr에 저장한다
    #ex)
    # 12 일때
    # 2로 먼저 나누고 arr을 6으로 다시 재할당

    for key in dict:
        while arr % key == 0:
            dict[key] += 1
            arr //= key

        print(f'#{tc} {dict[2]} {dict[3]} {dict[5]} {dict[7]} {dict[11]}')

        # if arr % 2== 0:
        #     dict[2]+=1
        #
        # elif arr % 3 ==0:
        #     dict[3] +=1
        #
        # elif arr % 5 == 0:
        #     dict[5] +=1
        #
        # elif arr % 7 ==0:
        #     dict[7] +=1
        #
        # elif arr % 11 ==0:
        #     dict[11] += 1

