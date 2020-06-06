import time

# chia de tri
def max_subarray(arr):
    smax = arr[0]
    maxendhere = arr[0]
    start = time.time()
    for i in range(1, len(arr)):
        u = maxendhere + arr[i]
        v = arr[i]
        if (u > v):
            maxendhere = u
        else:
            maxendhere = v
        if (maxendhere > smax):
            smax = maxendhere
    end = time.time()
    return smax, start, end


# dynamic programming
def max_subarray_dp(arr):
    dp = [0 for i in range(len(arr))]
    dp[0] = arr[0]
    start = time.time()
    for idx in range(1, len(arr)):
        dp[idx] = max(dp[idx-1] + arr[idx], arr[idx])
    end = time.time()
    return max(dp), start, end


arr = []
f = open("input", "r")
len_arr = int(f.readline())

for i in range(len_arr):
    data = f.read(i+1).strip()
    arr.append(int(data))

res1, st1, ed1 = max_subarray(arr)
res2, st2, ed2 = max_subarray_dp(arr)

f = open("output", "w")
f.write(f'ressult chia de tri: {res1}')
f.write(f'\n')
f.write(f'result quy hoach dong: {res2}')
f.write(f'\n')
f.write(f'time chia de tri: ')
f.write(f'\n')
f.write(f'start: {st1}      ')
f.write(f'end: {ed1}')
f.write(f'\n')
f.write(f'time quy hoach dong: ')
f.write(f'\n')
f.write(f'start: {st2}      ')
f.write(f'end: {ed2}')
f.close()
