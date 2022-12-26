'''
처음에 {{}}을 어떻게 없앨까 했는데 맨 처음 {{ 와 맨 뒤 }}을 없애주고 },{ 로 split을 해주면 깔끔하게 나눠진다.
그 이후 key = len으로 길이 기준으로 정렬한 뒤 stack으로 정답을 구한다.
여기서 길이기준 정렬한 이유는 길이가 작은거부터 큰거까지 들어간 순서대로이기 때문이다.
'''

def solution(s):
    answer = []
    
    s = s[2:-2]
    s = sorted(s.split('},{'),key=len)
    
    for i in s:
        ans = i.split(',')
        for j in ans:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer