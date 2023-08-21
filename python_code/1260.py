## 백준 1260번 문제
## 2023.08.02
## DFS와 BFS

import sys; input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
dfs_arr = []
dfs_visit = [False] * (N+1)
bfs_arr = []
bfs_visit = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

print(graph)

def dfs(graph, v, visited):
    # 처음 노드 방문 처리
    visited[v] = True
    # dfs결과 리스트에 추가
    dfs_arr.append(v)
    print(v, end=" ")

    # v 노드와 연결된 모든 노드에 대해서 탐색
    for i in graph[v]:
        # 연결된 노드가 방문한 적이 없다면 탐색
        # 아니면 탐색하지 않음
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visitied):
    # 큐를 생성하고 처음 노드를 푸시
    queue = deque([start])
    # 해당 노드 방문 처리
    visitied[start] = True

    while queue:
        # 큐의 맨 앞을 추출
        v = queue.popleft()
        print(v, end=" ")
        # bfs결과 리스트에 추가
        bfs_arr.append(v)

        # 연결된 노드 탐색
        for i in graph[v]:
            # 방문한 적이 없다면
            if not visitied[i]:
                # 큐에 넣어주고 방문처리
                queue.append(i)
                visitied[i] = True


dfs(graph, V, dfs_visit)
print()
bfs(graph, V, bfs_visit)