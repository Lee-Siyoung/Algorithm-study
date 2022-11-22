'''
일단 문자열이기 때문에 10을 구하기 쉽도록 a라는 임의로 숫자로 바꿔준 후 숫자일때 a배열에 넣어 특정 조건을 만족할때 식을 세워준다. 
어차피 넣어준 것들을 식으로 구성하기 때문에 [-1]로 맨 뒤에 것으로 구성하면 된다.
'''
def solution(dartResult):
    answer = 0
    a=[]
    dartResult = dartResult.replace('10', 'a')
    for i in range(len(dartResult)):
        if dartResult[i] in ['0','1','2','3','4','5','6','7','8','9','a']:
            if dartResult[i] == 'a':
                a.append(10)
            else:
                a.append(int(dartResult[i]))
        elif dartResult[i] == 'D':
            a[-1] = a[-1]**2
        elif dartResult[i] == 'T':
            a[-1] = a[-1]**3
        elif dartResult[i] == '*':
            if i == 2:
                a[-1] = a[-1] *2
            else:
                a[-1] = a[-1] *2
                a[-2] = a[-2] *2
        elif dartResult[i] == '#':
            a[-1] = -(a[-1])
    print(a)
    return sum(a)