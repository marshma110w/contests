n = int(input())
result = []
for i in range(n):
    f, i, o, d, m, y = input().split(',')

    uniq_fio_symbols = len(set(f + i + o))

    sr_sum = sum(map(int, d + m)) * 64
    f_number = (ord(f[0]) - ord('A') + 1) * 256
    ssum = uniq_fio_symbols + sr_sum + f_number

    result.append(format(ssum, 'X')[-3:].zfill(3))

print(' '.join(result))
