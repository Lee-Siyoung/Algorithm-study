'''
(1,2), (3,4), (5,6) ...로 붙는데 얘들은 몫과 나머지를 더하면 동일하다. 

1의 몫, 나머지 = 0 + 1 = 1

2의 몫, 나머지 = 1 + 0 = 1

위의 법칙대로 하면 된다.
'''
def solution(n,a,b):
    count=0
    while True:
        count+=1
        a = (a%2) + (a//2)
        b = (b%2) + (b//2)
        if a==b:
            return count