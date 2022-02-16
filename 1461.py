# 백준 1461번 문제
# 도서관
# 양수, 음수를 나누어 따로 계산

import re
import sys

N, M = map(int, sys.stdin.readline().split())

loc = list(map(int, sys.stdin.readline().split()))

# 리스트를 오름차순으로 정렬
loc.sort()

# 절대값이 제일 큰 수가 음수인지 양수인지 알기위함
if abs(loc[0]) >= abs(loc[-1]):
    max = loc[0]
else:
    max = loc[-1]

# 양수, 음수를 리스트를 나누어 저장
pos, neg = [], []

for i in loc:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

# 양수 값은 내림차순 정렬 -> 멀리 있는 책을 남기면 손해
pos.sort(reverse=True)

count = []

for i in range(0, len(neg), M):
    if neg[i] != max:
        count.append(abs(neg[i]))

for i in range(0, len(pos), M):
    if pos[i] != max:
        count.append(abs(pos[i]))

sum = 0

for i in count:
    sum += (2 * i)

sum += abs(max)

print(sum)