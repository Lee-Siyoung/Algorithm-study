'''
테스트 2처럼 중복될 경우를 위해 set으로 중복을 제거해준다. 그래야 시간초과가 안난다.

일단 신고한 사람과 신고 당한 사람을 알아야 하니 fromkeys으로 dict로 만들어 신고 id와 개수를 샌다.

신고 개수가 k값을 넘기면 lis에 id를 넣어줘 어떤 아이디가 정지되는지 확인한 후 set으로 변환해 교집합을 이용해 처리 결과 메일 개수를 센다.
'''

def solution(id_list, report, k):
    answer = []
    re=[]
    lis = []
    report=list(set(report))
    
    do = dict.fromkeys(id_list,'')
    done = dict.fromkeys(id_list,0)
    
    for i in report:
        re.append(i.split(" "))
    
    for i in id_list:
        for j in re:
            if i == j[0]:
                do[i] += j[1] + ' '
                done[j[1]] += 1
                
    for i in done:
        if done[i] >= k:
            lis.append(i)
        
    for i in do:
        a = do[i].split(" ")
        answer.append(len(set(lis)&set(a)))
    
    return answer