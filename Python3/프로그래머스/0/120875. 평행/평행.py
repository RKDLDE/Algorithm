def is_parallel(a, b, c, d):
    # 기울기 비교 (두쌍씩)
    return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0])

def solution(dots):
    return 1 if (
        is_parallel(dots[0], dots[1], dots[2], dots[3]) or
        is_parallel(dots[0], dots[2], dots[1], dots[3]) or
        is_parallel(dots[0], dots[3], dots[1], dots[2])
    ) else 0
