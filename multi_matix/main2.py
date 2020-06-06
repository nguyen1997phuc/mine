import sys


def matrix_chain_order(p, i, j):
    if i == j:
        return 0
    _min = sys.maxsize
    for k in range(i, j):
        count = (matrix_chain_order(p, i, k) + matrix_chain_order(p, k + 1, j) + p[i - 1] * p[k] * p[j])
        if count < _min:
            _min = count
            trace_back.append(k)
    return _min


arr = []
trace_back = []
f_input = open("nhan_ma_tran", "r")
len_arr = int(f_input.readline())
lines = f_input.readlines()

for line in lines:
    data = int(line)
    arr.append(int(data))

results = matrix_chain_order(arr, 1, len_arr - 1)

f = open("output_matrix", "w")
f.write(f'so phep nhan toi thieu la: {results}')
f.write(f'\n')
f.write(f'thu tu thuc hien la: ')
f.write(f'\n')
for item in trace_back:
    f.write(str(item))
f.close()

