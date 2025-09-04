def solution(rank, attendance):
    ranks = [(r, idx) for idx, (r, t) in enumerate(zip(rank, attendance)) if t]

    a, b, c = [idx for _, idx in sorted(ranks)[:3]]
    
    return 10000 * a + 100 * b + c