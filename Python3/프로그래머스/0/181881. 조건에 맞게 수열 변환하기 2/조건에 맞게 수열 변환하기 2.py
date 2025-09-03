def solution(arr):
    x = 0
    while True:
        # 복사
        arr2 = arr[:]
        
        # 조건
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        
        # 종료 조건(변환 전 = 변환 후)
        if arr == arr2:
            break
            
        # 인덱스 카운트
        x += 1
    return x