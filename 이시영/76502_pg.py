'''
이것도 stack문제인데 일단 deque.rotate로 회전을 시켜주면서 a라는 새로운 리스트를 선언한다.

그리고 괄호개수를 새는게 아니라 괄호가 만들어지는 개수이기 때문에 space = True로 True가 된 것에만 +1을 해주었다. 
a에 ([{를 넣어 괄호가 안만들어지면 space를 False로 했다. 
'''
from collections import deque
def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        s.rotate(-1)
        a=[]
        space = True
        for j in s:
            if j == '(' or j=='[' or j=='{':
                a.append(j)
            else:
                if not a:
                    space = False
                    break
                check = a.pop()
                if j == ')' and check  != '(':
                    space = False
                    break
                elif j == ']' and check  != '[':
                    space = False
                    break
                elif j == '}' and check  != '{':
                    space = False
                    break
        if space and not a :
            answer+=1
                    
    return answer