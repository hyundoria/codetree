n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [10000] * (m+1)
dp[0] = 0

for i in range(n):
    for j in range(m, 0, -1):
        if j - arr[i] >= 0:
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

if dp[m] == 10000:
    print(-1)
else:
    print(dp[m])