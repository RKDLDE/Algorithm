def solution(arr, intervals):
    return [arr[i] for start, end in intervals for i in range(start, end+1)]
