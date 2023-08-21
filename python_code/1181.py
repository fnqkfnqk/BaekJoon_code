# 백준 1181번
# 단어 정렬

import sys; input = sys.stdin.readline

n = int(input().rstrip())

arrInput = []
arrResult = []

for _ in range(n):
    text = input().rstrip()
    arrInput.append([text, len(text)])

arrInput.sort(key=lambda x:x[0])
arrInput.sort(key=lambda x:x[1])

for i in range(n):
    if(arrInput[i][0] not in arrResult):
        arrResult.append(arrInput[i][0])

for i in arrResult:
    print(i)