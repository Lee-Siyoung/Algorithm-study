def solution(s):
    a=[]
    for i in s:
        if len(a)==0:
            a.append(i)
        elif i == a[-1]:
            a.pop()
        else:
            a.append(i)
    if len(a)==0:
        return 1
    return 0