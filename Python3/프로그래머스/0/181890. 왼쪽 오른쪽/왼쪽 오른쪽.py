# def solution(str_list):
#     str = ''.join(str_list)
#     l_find = 21 if str.find('l') == -1 else str.find('l')
#     r_find = 21 if str.find('r') == -1 else str.find('r')
    
#     if l_find == 21 and r_find == 21:
#         return []
#     else:
#         if l_find < r_find:
#             return str_list[:l_find]
#         else:
#             return str_list[r_find:]

def solution(str_list):
    for i, ch in enumerate(str_list):
        if ch == "l":
            return str_list[:i]
        if ch == "r":
            return str_list[i+1:]
    return []