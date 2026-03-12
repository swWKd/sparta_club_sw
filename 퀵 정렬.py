T = int(input())
for tc in range(1, T+1):
    N =int(input())
    arr = list(map(int, input().split()))

    #A: 정렬할 배열
    #l, r: 정렬 배열의 시작 인덱스, 종료 인덱스
    def quicksort(A, l, r):
        if l < r:
            #기준 원소를 정해서 기준원소(피벗)의 위치를 확정
            p = partition(A, l, r)

            #기준 원소(피벗)의 왼쪽을 다시 퀵 정렬
            quicksort(A, l, p-1)

            #기준 원소(피벗)의 오른쪽을 다시 퀵 정렬
            quicksort(A, p+1, r)

    def partition(A, l, r):
        #l~ r이 부분을 파티셔닝
        # 기준 원소(피벗)을 하나 정하자. ->가장 왼쪽에 있는 친구
        p= A[l]

        #p보다 작은 애는 왼쪽으로
        #p보다 큰 애는 오른쪽으로

        #왼쪽에서 p보다 큰 애를 찾고 오른쪽에서 p보다 작은 애를 찾아
        # 자리를 서로 교환 시키자.

        # i는 왼쪽에서 시작해서 큰 애를 찾을 때까지 오른쪽으로 간다.
        i = l
        # r은 오른쪽에서 시작해서 작은 애를 찾을 때까지 왼쪽으로 간다.
        j = r

        #i와 j가 교차하기 전까지 찾아라
        while i <=j:
            #i는 왼쪽에서 +1
            while i <= j and A[i] <=p:
                i += 1
            #j는 오른쪽에서 -1
            while i <=j and A[j] >= p:
                j -=1

            # 위에 있는 두개의 while이 끝나고 나서
            # 여전히 i가 j보다 작으면
            # 잘못된 위치에 있는 원소를 찾은거다 -> 자리교환
            if i < j:
                A[i], A[j] = A[j], A[i]

        #i와 j가 교차하면 반복 종료
        # 왼쪽 부분에는 p보다 작은 애들이 모여있고(정렬 x)
        # 오른쪽 부분에는 p보다 큰 애들이 모여있는 상태(정렬X)

        #왼쪽 부분과 오른쪽 부분의 경계에 p를 꽂아주면 종료
        # i와 j가 교차하면 i는 큰 원소들의 인덱스, j는 작은 원소들의 인덱스
        # p는 누구랑 자리를 바꿔야 하나? p는 가장 왼쪽, 작은 부분에 속해있었으므로 j랑 바꿔야 함.
        A[l], A[j] = A[j], A[l]

        #기준 원소의 자리는 j로 확정(FIX)
        return j

    quicksort(arr, 0, len(arr) -1)
    print(f"#{tc} {arr[N//2]}")