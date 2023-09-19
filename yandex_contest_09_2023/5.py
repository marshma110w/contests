from collections import defaultdict

def combinations(n):
    return (n ** 2 - n) // 2

n = int(input())


arrays = []
lengths = [0] * n
groups = defaultdict(list)


for i in range(n):
    lengths[i] = int(input())
    arrays.append(tuple(map(int, input().split())))

for ar_index in range(len(arrays)):
    groups[(arrays[ar_index][0],)].append(ar_index)

ans = 0

ans += sum(combinations(len(x)) for x in groups.values()) 

i = 1
while True:
    new_groups = defaultdict(list)
    for pre_prefix, group in groups.items():
        for array_id in group:
            if i < lengths[array_id]:  
                new_groups[tuple(list(pre_prefix) + [arrays[array_id][i]])].append(array_id)
    
    exit = True
    for group in groups.values():
        if len(group) > 1:
            exit = False
            break
    if exit:
        break

    groups = new_groups
    ans += sum(combinations(len(x)) for x in groups.values())
    i += 1


print(ans)