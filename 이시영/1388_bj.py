'''
dfs, bfs로 풀 수 있는데 나는 다르게 풀었다.
문제에서 -, | 두 경우 나눠 풀 수 있는데 -는 가로, |는 세로에 해당하는 부분이라 각각 나눠 푼다.
flag를 세워 이전 값과 현재 값이 다를 경우 개수를 더해준다.
'''
from sys import stdin

a, b = map(int, stdin.readline().split())

dep = [list(map(str, stdin.readline().rstrip())) for _ in range(a)]
num=0
for i in range(a):
    flag = '?'
    for j in range(b):
        if dep[i][j]=='-' and dep[i][j]!=flag:
            num+=1
        flag=dep[i][j]

for i in range(b):
    flag = '?'
    for j in range(a):
        if dep[j][i]=='|' and dep[j][i]!=flag:
            num+=1
        flag=dep[j][i]
print(num)