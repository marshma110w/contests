n = int(input())
arrays = []
lengths = []
for _ in range(n):
    lengths.append(int(input()))
    arrays.append(tuple(map(int, input().split())))

allowed_pairs = []
for i in range(n):
    for j in range(i + 1, n):
        allowed_pairs.append((i, j))

res = 0
i = 0
while allowed_pairs:
    for j in range(len(allowed_pairs) - 1, -1, -1):
        a, b = allowed_pairs[j]
        if i >= lengths[a] or i >= lengths[b] or arrays[a][i] != arrays[b][i]:
            allowed_pairs.pop(j)
        else:
            res += 1
    i += 1

# (1, 2, 3, 4, 5, 0, 0, 0, 0),
# (1, 2, 6, 4, 5),
# (1, 2, 3, 4, 5, 7)


print(res)
