def solution(s):
    a=[]
    for i in s:
        if i == '(':
            a+=i
        elif not a or a.pop()!='(':
            return False
    if a:
        return False
    else:
        return True