n = int(input())
count = n

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]: # 뒤에 단어가 연속이면
            continue
        elif word[i] in word[i+1:]:# 뒤에 동일 단어가 나타나면
            count -= 1
            break
print(count) 