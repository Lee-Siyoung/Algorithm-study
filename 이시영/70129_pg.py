def solution(s):
    i,count=0,0
    while s != '1':
        if '0' in s:
            count += s.count('0')
            s = s.replace('0','')
        s = str(bin(len(s))[2:])
        i += 1
    return [i,count]