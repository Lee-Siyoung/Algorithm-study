'''
dict로 각 성격 유형의 값이 나올때 더해주고 RT, CF, JM, AN끼리 값을 비교해 값을 구했다.
'''
def solution(survey, choices):
    answer = ''
    a ={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    bad = [3,2,1]
    good = [5,6,7]
    
    for i in range(len(survey)):
        if choices[i] in bad:
            a[survey[i][0]]+=bad.index(choices[i])+1
        elif choices[i] in good:
            a[survey[i][1]]+=good.index(choices[i])+1
    
    lis = [['R','T'],['C','F'],['J','M'],['A','N']]
    
    for i in lis:
        if a[i[0]] >= a[i[1]]:
            answer += i[0]
        else :
            answer += i[1]
    
    return answer