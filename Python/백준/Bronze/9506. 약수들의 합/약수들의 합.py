while True:
    N = int(input())
    arr = []
    
    if N == -1:
        break

    for i in range(1, N):
        if N % i == 0:
            arr.append(i)

    if N == sum(arr):
        print(f"{N} = {' + '.join(map(str,arr))}")
    else:
        print(f"{N} is NOT perfect.")