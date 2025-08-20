def solution(code):
    mode = False
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
            continue
        if mode and i % 2 != 0:
            ret += code[i] 
        elif not mode and i % 2 == 0:
            ret += code[i]
        
    return "EMPTY" if ret == '' else ret