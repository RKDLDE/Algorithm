def solution(s):
    return True if s.isdecimal() and len(s) in [4, 6] else False