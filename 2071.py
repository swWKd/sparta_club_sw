# 내장함수 쓰는 첫 번째 방법
T= int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))   # 문제에서 테스트 케이스 3개 나왔고
                                            # 한 줄에 공백으로 숫자들이 구분되어 있어 이렇게 받는다.

    plus = 0    # 합을 구하기 위한 변수
    num = 0     # 원소의 갯수를 알기 위한 변수(평균을 구할 때 갯수를 나눠야함)
    for i in range(10):     # 문제에서 10개의 수를 입력 받는다고 함
        plus += arr[i]      # 평균을 구하기 위해선 1. 합을 구해야함
        num += 1            # 평균을 구하기 위해선 2. 갯수를 알아야함
        a = round(plus / num, )
        # round는 반올림을 해주는 것이다.
        # , 뒤에 소수점 몇째자리까지 보여주고 싶은지를 표시하는 것
        # 나는 소수점 첫번째자리에서 반올림하고 정수로 표현하고 싶어서
        # 공백으로 둔 것이다.
        # 주의: round(sum/num, )만 하고
        # 프린트에 {round}라고 적으면 출력이 되지 않는다!!!!
        # 반드시 변수에 담아야 함!!!

    print(f"#{tc} {a}")


# #내장함수 안쓰는 두 번째 방법
# T = int(input())
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#
#     plus = 0
#     num = 0
#     for i in range(10):
#         plus += arr[i]
#         num += 1
#
#     a= plus / num   #소숫점까지 나오는 평균을 a로 지정
#
#     int_only = a // 1   # 소숫점까지 나오는 평균에 몫나눗셈을 하면 정수부분만 나오게 됨.
#                         # ex) 24.2 // 1 == 24.0 (타입이 float이기에 결과도 저렇게 나옴)
#     b = a - int_only    # 이렇게 하면 소숫점만 나오게 됨.
#                         # 이걸 하는 이유는 0.5 이상이면 올림을 하고
#                         # 0.5 미만이면 버릴려고 하기 때문
#
#     if b >= 0.5:
#         answer = int_only + 1
#     else:
#         answer = int_only
#     answer = int(answer)  # 이걸 안붙이면 결과값에 24.0 처럼 .0이 붙어 나옴
#
#     print(f"#{tc} {answer}")