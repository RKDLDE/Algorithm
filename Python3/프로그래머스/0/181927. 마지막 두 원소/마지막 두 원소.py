def solution(num_list):
    a = num_list[-1] - num_list[-2]
    b = num_list[-1] * 2
    num_list.append(a) if num_list[-1] > num_list[-2] else num_list.append(b)
    return num_list