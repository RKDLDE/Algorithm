def solution(arr):
    row = len(arr)
    col = len(arr[0])
    
    if row > col:
        for a in arr:
            a.extend([0] * (row-col))
    else:
        arr.extend([[0] * col] * (col-row))
            
    return arr