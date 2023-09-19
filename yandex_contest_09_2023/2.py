from collections import defaultdict

q = int(input().split()[2])

a = defaultdict(int)
b = defaultdict(int)

for card in input().split():
    a[card] += 1

for card in input().split():
    b[card] += 1

difference = 0
for card in set(list(a.keys()) + list(b.keys())):
    difference += abs(a[card] - b[card])

for _ in range(q):
    change, player, card = input().split()
    
    if player == 'A':
        if change == "1":
            if a[card] >= b[card]:
                difference += 1            
            else:
                difference -= 1
            a[card] += 1

        else:
            if a[card] > b[card]:
                difference -= 1
            else:
                difference += 1
            a[card] -= 1

    else:
        if change == "1":
            if b[card] >= a[card]:
                difference += 1
            else:
                difference -= 1
            b[card] += 1
            
        else:
            if b[card] > a[card]:
                difference -= 1
            else:
                difference += 1
            b[card] -= 1
      
    print(difference, end=' ')
    

