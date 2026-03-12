T = int(input())
for tc in range(1, T+1):
    # 정수의 개수
    N = int(input())
    # N개의 정수를 arr 리스트로 받기
    arr = list(map(int, input().split()))


    #병합정렬 함수
    #정렬할 범위를 지정(인덱스)
    #시작(start) ~ 끝(end)

    cnt = 0
    def merge_sort(start, end):
        global cnt

        #1. 종료 조건
        # 원소가 하나 남았을 때
        # 더 이상 분할이 불가능함
        if start == end -1:
            return start, end

        #2. 재귀호출
        # 두 부분으로 나누고
        # 합칠 때 정렬이 이루어진다.
        # 두 부분으로 나누는 기준은 가운데
        mid = (start + end) //2

        #왼쪽 부분 다시 분할 후 정렬
        left_s, left_e = merge_sort(start, mid)
        # 오른쪽 부분 다시 분할 후 정렬
        right_s, right_e = merge_sort(mid, end)


        #if 왼쪽 부분 정렬 후 마지막 원소 > 오른쪽 부분 정렬 후 마지막 원소:
        if arr[left_e-1] > arr[right_e-1]:
            cnt += 1

        #합치면 됨
        merge(left_s, left_e, right_s, right_e)
        #정렬된 범위 리턴
        return start, end

    def merge(left_s, left_e, right_s, right_e):

        #왼쪽 부분의 가장 작은 원소가 있는 인덱스
        l = left_s
        #오른쪽 부분의 가장 작은 원소가 있는 인덱스
        r = right_s

        #왼쪽 부분과 오른쪽 부분을 합친 길이
        L = right_e - left_s
        result = [0] * L

        # result배열에 들어갈 원소의 다음 자리(작은순서)
        idx = 0

        while l< left_e and r< right_e:
            if arr[l] < arr[r]:
                # 왼쪽 부분의 맨 앞에 최소값이 있다.
                result[idx] = arr[l]
                l +=1
                idx += 1

            else:
                # 오른쪽 부분의 맨 앞에 최소값이 있다.
                result[idx] = arr[r]
                r += 1
                idx += 1

        # 둘 중 한 부분에만 원소가 남아 있는 경우
        # 남아있는 원소 주루룩 추가

        # 오른쪽만 남은 경우
        while r < right_e:
            result[idx] = arr[r]
            r += 1
            idx += 1

        #왼쪽만 남은 경우
        while l < left_e:
            result[idx] = arr[l]
            l += 1
            idx += 1


        # result 안에는 left_s에서 right_e까지의 원소들이
        # 오름차순으로 정렬이 되어있고, 이 부분을 원본 arr에 반영
        for i in range(L):
            arr[left_s + i] = result[i]
        # print(result[N//2])

    merge_sort(0, N)
    print(f"#{tc} {arr[N//2]} {cnt}")

