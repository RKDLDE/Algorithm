word_list=[]

for i in range(5):
    word = str(input())
    word_list.append(list(word))

for col in range(max(len(row) for row in word_list)):
    for row in range(len(word_list)):
        if col < len(word_list[row]):
            print(word_list[row][col], end='')