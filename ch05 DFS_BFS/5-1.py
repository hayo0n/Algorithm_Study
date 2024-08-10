# 음료수 얼려 먹기
n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if graph[x][y]==0: # 0으로 표시된 영역을 찾으면 해당 영역의 모든 점을 1로 바꿈
        graph[x][y]=1
        dfs(x-1,y) # 해당 점의 상하좌우를 탐색하여 모든 0을 1로 바꾸는 것을 반복
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
for i in range(n): # 모든 그래프의 점을 시작점으로 DFS 수행
    for j in range(m):
        if dfs(i,j)==True:
            result+=1 # 영역의 개수를 셈

print(result)