'''
set 차집합으로 먼저 lost와 reserve에 중복되는 값을 없애주었다. 
즉, 여벌 체육복이 있는 학생이 도난당했을 경우이다.
'''

def solution(n, lost, reserve):
    answer = 0
    a = set(lost)
    b = set(reserve)
    lost = list(a - b)
    reserve = list(b - a)
    for i in lost:
        a = i-1
        b = i+1
        if a in reserve:
            reserve.pop(reserve.index(a))
        elif b in reserve:
            reserve.pop(reserve.index(b))
        else:
            n-=1
    
    return n