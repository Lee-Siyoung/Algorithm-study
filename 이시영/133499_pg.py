def solution(babbling):
    answer = 0
    for i in babbling:
        a=''
        b=''
        for j in range(len(i)):
            a+=i[j]
            if a in ["aya", "ye", "woo", "ma"] and a != b:
                b=a
                a=''
        if len(a) == 0:
            answer+=1
    
    return answer