def solution(num_list):
    return next((i for i, v in enumerate(num_list) if v < 0), -1)