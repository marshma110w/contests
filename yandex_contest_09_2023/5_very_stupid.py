n = int(input())


arrays = []
lens = [0] * n
for i in range(n):
    lens[i] = int(input())
    arrays.append(tuple(map(int, input().split())))

res = 0
for i in range(n):
    for j in range(i+1, n):
        k = 0
        while k < lens[i] and k < lens[j] and arrays[i][k] == arrays[j][k]:
            k += 1
        res += k

print(res)        