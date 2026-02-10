T= int(input())
for tc in range(1, T+1):
    arr= list(map(int, input().split()))    #문제에서는 테스트케이스 3개에 각 줄 마다
                                            # 숫자가 공백으로 구분되어 나와있음.
                                            # 따라서 이들을 일단 리스트로 받음!

    plus = 0    #홀수만 더한 값을 구하기 위해 변수 지정
    for i in range(10): #문제에서 10개의 수를 받는다고 함
        if arr[i] % 2 == 1: #range(10)하면 인덱스 번호가 나옴
                            # 따라서 arr[i] 형태로 해서 나누기 했을 때 나머지가 1인게 홀수
            plus += arr[i]  # 홀수들 다 더하기

    print(f"#{tc} {plus}")