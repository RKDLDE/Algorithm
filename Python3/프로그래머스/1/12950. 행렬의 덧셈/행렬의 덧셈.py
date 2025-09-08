def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        add = []
        for j in range(len(arr1[i])):
            add.append(arr1[i][j] + arr2[i][j])
        answer.append(add)

    return answer