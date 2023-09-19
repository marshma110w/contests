n = int(input())
langs =  ['X'] + input().split()
nums = list(map(int, input().split()))

a_stack = [0]
b_stack = [0]
stack = set()
ans = {}

for number in nums[1:]:
    lang = langs[number]

    if number not in stack:
        stack.add(number)
        if lang == 'A':
            ans[number] = a_stack[-1]
            a_stack.append(0)
            b_stack[-1] += 1

        elif lang == 'B':
            ans[number] = b_stack[-1]
            b_stack.append(0)
            a_stack[-1] += 1

    else:
        stack.remove(number)
        if lang == 'A':
            a_stack.pop()
            b_stack[-1] -= 1
        elif lang == 'B':
            b_stack.pop()
            a_stack[-1] -= 1


for i in range(1, n+1):
    print(ans[i], end = ' ')
