from math import gcd
def solution(num1, num2):
    answer=[]
    gcd1, gcd2 = num1[0], num2[0]
    for a, b in zip(num1[1:], num2[1:]):
        gcd1, gcd2 = gcd(a, gcd1), gcd(b, gcd2)
    
    for i in num1:
        if i%gcd2 == 0:
            break
    else:
        answer.append(gcd2)
    for i in num2:
        if i%gcd1 == 0:
            break
    else:
        answer.append(gcd1)
        
    if answer:
        return max(answer)
    else:
        return 0