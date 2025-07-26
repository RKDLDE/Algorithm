import collections

def solution(array):
    freq  = collections.Counter(array).most_common()
    
    max_freq  = freq [0][1]
    count = 0
    for key, value in freq :
        if max_freq  == value:
            count += 1
    
    if count == 1:
        return freq [0][0]
    elif count >= 2:
        return -1