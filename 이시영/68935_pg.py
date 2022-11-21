def solution(n):
    answer = ''
    m=3
    while n>0:
        n, mod = divmod(n,3)
        answer +=str(mod)
    answer=int(answer,3)
    
    
    return answer