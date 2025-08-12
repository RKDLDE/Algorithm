def solution(myString, pat):
    table = myString.maketrans("AB", "BA")
    myString = myString.translate(table)
    return 1 if pat in myString else 0