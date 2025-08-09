def solution(s):
    return " ".join(
        word.capitalize() if word and not word[0].isdigit() else word.lower()
        for word in s.split(" ")
    )