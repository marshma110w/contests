n = int(input())
languages =  [''] + input().split()
nums = list(map(int, input().split()))

stack_a = [0]
stack_b = [0]
stack = set()
ans = [''] * n

for number in nums[1:]:
    language = languages[number]

    if number not in stack:
        stack.add(number)
        if language == 'A':
            ans[number - 1] = str(stack_a[-1])
            stack_b[-1] += 1
            stack_a.append(0)

        elif language == 'B':
            ans[number - 1] = str(stack_b[-1])
            stack_a[-1] += 1
            stack_b.append(0)

    else:
        if language == 'A':
            stack_b[-1] -= 1
            stack_a.pop()
        elif language == 'B':
            stack_a[-1] -= 1
            stack_b.pop()
        stack.remove(number)


print(' '.join(ans))
