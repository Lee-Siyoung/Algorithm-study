def solution(s):
    try:
        a=list(map(int,s))
        if len(a) == 4 or len(a)==6:
            return True
        else:
            return False
    except ValueError:
        return False
    return True