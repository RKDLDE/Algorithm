N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

def get_index(index):
    return B[index]
    
B_index = sorted(range(len(B)), key=get_index, reverse=True)

result = 0
for i in range(N):
    result += B[B_index[i]] * A[i]
print(result)