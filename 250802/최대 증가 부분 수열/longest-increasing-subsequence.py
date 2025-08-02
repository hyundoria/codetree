import sys

INT_MIN = -sys.maxsize

n = int(input())

sequence = list(map(int, input().split()))

dp = [INT_MIN] * n
dp[0] = 1

for i in range(n):

    for j in range(i):
        
        if dp[j] == INT_MIN:
            continue
        
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))