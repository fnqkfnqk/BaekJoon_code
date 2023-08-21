# 백준 11728 문제
# 배열 합치기
import sys; input = sys.stdin.readline

n, m = map(int, input().split())

arrayN = list(map(int, input().split()))
arrayM = list(map(int, input().split()))

arrayN += arrayM

arrayN.sort()

print(*arrayN)