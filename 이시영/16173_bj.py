'''
방문한지 안한지 visited로 구분해 점프했을때의 재귀함수로 해서 넘어가면 False하고 값이 -1이 된다면
HaruHaru를 해주고 exit()로 끝낸다.
'''
from sys import stdin

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    if x >= n or y >= n:
        return False

    jump = graph[x][y]
    if jump == -1:
        print("HaruHaru")
        exit(0)
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x + jump, y)  
        dfs(x, y + jump) 

dfs(0, 0)
print('Hing')