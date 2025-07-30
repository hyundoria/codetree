n = int(input())

count = []

ans = []

def get(num):

    if num == n+1:

        cnt = 0

        if ans[0] != 1:
            cnt = 1

        for i in range(1, n):
            
            if ans[i-1] == ans[i]:
                cnt += 1
                
                cnt = cnt % ans[i]
            else:
                if cnt != 0:
                    return
                else:
                    if ans[i] != 1:
                        cnt += 1

        if cnt != 0:
            return
        
        count.append(1)
        return


    for i in range(1, 5):
        ans.append(i)
        get(num+1)
        ans.pop()


    return

get(1)
print(len(count))