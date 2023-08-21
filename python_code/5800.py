# 백준 5800번
# 성적 통계

import sys; input = sys.stdin.readline

n = int(input().rstrip())

score = []
lGap = [-1] * n

for _ in range(n):
    score.append(list(map(int, input().split())))

for i in range(n):
    score[i].sort()

for i in range(n-1):
       

print(lGap)
print(score)