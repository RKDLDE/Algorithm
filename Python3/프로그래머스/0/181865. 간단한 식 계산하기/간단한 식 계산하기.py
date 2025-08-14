def solution(binomial):
    if "+" in binomial:
        return sum(int(i) for i in binomial.split("+"))
    elif "-" in binomial:
        return int(binomial.split("-")[0]) - int(binomial.split("-")[1])
    else:
        return int(binomial.split("*")[0]) * int(binomial.split("*")[1])
    