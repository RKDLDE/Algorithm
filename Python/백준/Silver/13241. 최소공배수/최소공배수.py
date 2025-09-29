# 최소공배수 = 두자연수의 곱 / 최대공약수
import math

a, b = map(int, input().split())
# 유클리드 호제법
# 두 수가 서로 상대방 수를 나누어서 원하는 수를 얻는 알고리즘
# a와 b의 최대공약수는 b와 r의 최대공약수와 같음

def gdc(a, b):
    while b > 0:
        a, b = b, a % b
    return a

print(int((a * b) / gdc(a, b)))