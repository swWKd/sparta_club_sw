# 첫 번째 줄에 스위치 갯수 = s_cnt
s_cnt = int(input())
# 두 번째 줄에 각 스위치의 상태 = arr
arr= list(map(int, input().split()))
# 셋째 줄에는 학생 수 = student
student = int(input())
# 넷째 줄부터 마지막 줄까지 한줄에 한 학생의 성별, 학생이 받은 수
# 이때 학생의 수는 student
# s는 학생의 성별
# 남자는 1, 여자는 2
# num은 학생이 받은 수
for _ in range(student):
    s, num = map(int, input().split())


    #남자인 경우
    #자기가 받은 수의 배수이면, 스위치 상태 바꾸기
    # 만약 s가 1이라면(남자라면)
    # 전체 스위치 갯수만큼 반복할건데
    # 만약 너의 번호로 나누었을 때 나머지가 0이라면
    # 즉, 부여받은 번호의 배수라는 말
    # 스위치 상태를 바꿔라
    # 스위치 상태가 0 이면 1로
    # 스위치 상태가 1이면 0으로
    # 이때 주의 할 점!!
    # 스위치 번호는 1부터 시작하지만
    # arr 인덱스는 0부터 시작하므로
    # (i+1) % num을 해야 스위치번호 % 부여받은 번호가 됨
    if s == 1:
        for i in range(s_cnt):
            if (i+1) % num == 0:
                if arr[i] == 0:
                    arr[i] = 1
                elif arr[i] == 1:
                    arr[i] = 0

    # 여자인 경우
    # s==2 라면
    # 여기도 동일하게 스위치 번호는 1이지만
    # arr의 인덱스는 0부터 시작한다
    #따라서 여자가 부여받은 num의 인덱스 번호는 num -1임
    # 그걸 기준으로 좌우를 봐야하니
    # 먼저 변수 center로 중심 지정
    # 왼쪽과 오른쪽도 center와 동일하게 지정해둔다
    # 그리고 우리가 좌우가 얼마나 같은지 즉, 스위치 상태를 몇 번 바꿔야할지 모르므로
    # for문이 아닌 while문 사용
    if s == 2:
        center = num -1
        left = center
        right = center
        while True:
            # 특히 이때 왼쪽 인덱스 번호는 0이상이어야 하고
            # 오른쪽 인덱스 번호는 스위치의 갯수보다 작아야한다
            # 그 이유는 스위치 갯수는 1부터 시작하니깐 s_cnt보다 작아야함
            # 그럼 그 범위 안에 들면서 좌우가 같다면
            # 그 옆에 있는 좌우를 확장시켜 나가면서 확인해야함
            if 0 <= left -1 and right + 1< s_cnt:
                if arr[left-1] == arr[right+1]:
                    left -= 1
                    right += 1
                # 만약 좌우가 같지 않다면 그만 멈춰!
                else:
                    break
            # 범위 안에 있지 않다면 멈춰!! 볼 필요가x
            else:
                break
        # 이제 while문을 통해 확인한 좌우를 보고
        # 스위치 상태를 바꿔야 함
        # 이때 범위는 left인덱스부터 right+1까지
        # 이유는 left를 점점 줄여나갔고 그 인덱스부터 시작해서
        # right도 계속 확장해 나갔는데 range는 end-1값 인덱스까지니
        #left인덱스부터 right+1인덱스까지 범위로 지정
        for i in range(left, right+1):
            # 그 인덱스 번호의 스위치 상태가 1이라면
            # 0으로 바꾸기
            if arr[i] == 1:
                arr[i] = 0
            #1이 아니라면(0이라면)
            # 1로 바꾸기
            else:
                arr[i] = 1

# 이때 출력을 20개까지 쓰고
# 21번부턴 두번째 줄에 작성을 해달라고 했으니
# 범위를 정해서 프린트
# 이때 리스트가 아니고 숫자만 나와있으므로 언패킹 * 해서 답을 출력
for i in range(0, s_cnt, 20):
    print(*arr[i: i+20])