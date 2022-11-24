'''
LRU(Least Recently Used)를 구현하는 문제이다.
'''
def solution(cacheSize, cities):
    answer = 0
    a=[]
    for i in cities:
        i = i.lower()
        if i in a:  # cache hit
            a.remove(i)
            a.append(i)
            answer+=1
        else: # cache miss
            if len(a) < cacheSize:
                a.append(i)
            elif len(a) == cacheSize:
                a.append(i)
                a.pop(0)
            answer+=5
    return answer