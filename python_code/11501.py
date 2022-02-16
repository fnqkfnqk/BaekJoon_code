#백준 11501문제 
# 큐를 사용하여 문제 해결


import sys

test = int(sys.stdin.readline().strip())

for _ in range(test):
    day = int(sys.stdin.readline().strip())

    stock = list(map(int, sys.stdin.readline().split()))

    sum = 0

    while True:
        if len(stock) == 0:
            break
        # 실제 stock리스트에는 변화가 없음    
        num = stock.pop()

        for j in range(len(stock) - 1, -1 , -1):
            if num >= stock[j]:
                sum += (num - stock[j])
                stock.pop()
            else:
                break
    
    print(sum)
