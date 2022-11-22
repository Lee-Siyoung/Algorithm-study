def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        if budget >= i:
            answer +=1
            budget -= i
    return answer