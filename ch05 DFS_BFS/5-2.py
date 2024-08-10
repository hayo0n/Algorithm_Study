# 미로 탈출
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

from collections import deque

dx=[-1,1,0,0] # 방향 지정
dy=[0,0,-1,1]

def bfs(x,y): # 시작점-도착점까지의 최단거리 계산
    queue=deque()
    queue.append((x,y)) # 시작점을 큐에 추가
    while queue:
        x,y=queue.popleft() # 큐에서 하나의 위치를 가져옴
        for i in range(4): # 현재 위치에서 상하죄우로 이동
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue # 그래프 범위 벗어나는 경우 무시
            if graph[nx][ny]==0:
                continue # 벽인 경우 무시
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1 # 이동할 수 이는 경우, 이전 위치에서의 거리에 1을 더해 거리 갱신
                queue.append((nx,ny)) # 이동할 수 있는 위치(다음 위치) 큐에 추가
    return graph[n-1][m-1] # 도착점까지의 최단 거리 반환

print(bfs(0,0))