import sys

INT_MAX = sys.maxsize

n, m  = map(int, input().split())

coin = list(map(int, input().split()))

dp = [INT_MAX] * (m+1)
dp[0] = 0

for i in range(1, m+1):
    for c in coin:

        if i-c < 0:
            continue
        
        dp[i] = min(dp[i-c] + 1, dp[i])
        

if dp[m] == INT_MAX:
    print(-1)
else:
    print(dp[m])

