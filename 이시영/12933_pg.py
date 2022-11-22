def solution(n):
    answer = 0
    n = sorted(list(str(n)),reverse=True)
    n = ''.join(n)
    return int(n)