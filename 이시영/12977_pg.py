'''
소수 판별 함수를 만들어 조합을 이용해 3개의 수를 구해 함수를 이용해 판별했다. 

소수 판별 함수는 시간 복잡도를 최소화 하도록 만들었다.
'''
from itertools import combinations

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False  
    return True

def solution(nums):
    answer = 0
    
    nums = list(combinations(nums,3))
    for i in nums:
        if isprime(sum(i)) == True:
            answer+=1
    return answer