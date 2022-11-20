'''
약수를 구하는 함수를 한다면 시간초과로 틀렸다고 나온다. 
그래서 약수의 성질을 이용해 시간초과를 줄여주도록 했다.
'''
def a(n):
    num = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            num+=1
            if (i**2)!=n : 
                num+=1
    return num

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        if a(i) > limit:
            answer+=power
        else:
            answer+=a(i)

    return answer