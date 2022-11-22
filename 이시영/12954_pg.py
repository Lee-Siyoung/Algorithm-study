def solution(x, n):
    answer = []
    answer.append(x)
    a=x
    for _ in range(n-1):
        answer.append(x+a)
        x+=a
    return answer