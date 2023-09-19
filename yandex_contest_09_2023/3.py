n, m, q = map(int, input().split())

names_list = input().split()
names = {}
table = []

for i in range(m):
    names[names_list[i]] = i


for i in range(n):
    table.append(tuple(map(int, input().split())))


upper_bounds = { i: 10 ** 9 + 1 for i in range(m) }
lower_bounds = { i: -1 * 10 ** 9 - 1 for i in range(m) }


for i in range(q):
    condition = input().split()
    column_id = names[condition[0]]
    if condition[1] == '<':
        upper_bounds[column_id] = min(upper_bounds[column_id], int(condition[2]))
    else:
        lower_bounds[column_id] = max(lower_bounds[column_id], int(condition[2]))

res_sum = 0
for row in table:
    take = True
    for col_id in upper_bounds:
        if row[col_id] >= upper_bounds[col_id]:
            take = False
            break
    for col_id in lower_bounds:
        if row[col_id] <= lower_bounds[col_id]:
            take = False
            break
    if take:
        res_sum += sum(row)

print(res_sum)