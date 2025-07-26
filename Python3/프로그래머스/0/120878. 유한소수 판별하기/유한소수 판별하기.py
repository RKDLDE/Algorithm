import math

def solution(a, b):
    gcd = math.gcd(a, b) # 최대공약수
    
    # 기약분수 만들기
    a //= gcd
    b //= gcd
    
    # 분모의 소인수
    for i in [2, 5]:
        while b % i == 0:
            b //=i
            
    if b == 1:
        return 1
    else:
        return 2

