# 백준 2109번 문제
# 순회강연
# 강의료가 높은 순으로 날짜를 채운다

import sys

# 강의날짜 배열을 0으로 초기화
visit_day = [0] * 100001

n = int(sys.stdin.readline().rstrip())

pay = []

for _ in range(n):
    money, day = map(int, sys.stdin.readline().rstrip().split())
    pay.append([money, day])

# 페이를 기준으로 내림차순으로 정렬
pay.sort(key = lambda pay: -pay[0])

sum = 0

for i in range(n):
    for j in range(pay[i][1], 0, -1):
        if visit_day[j] == 0:
            sum += pay[i][0]
            visit_day[j] = 1
            break

print(sum)