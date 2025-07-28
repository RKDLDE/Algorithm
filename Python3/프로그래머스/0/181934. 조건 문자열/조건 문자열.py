def solution(ineq, eq, n, m):
    op = ineq + eq
    compare = {
        '<=': lambda a, b: a <= b,
        '<!':  lambda a, b: a < b,
        '>=': lambda a, b: a >= b,
        '>!':  lambda a, b: a > b,
    }
    if eq == '':
        op = ineq
    return int(compare[op](n, m))