class Tree:
    class Node:
        def __init__(self):
            self.amount = 1
            self.children = {}

    def __init__(self):
        self.head = self.Node()
        self.sum = 0

    def add(self, array):
        current_node = self.head
        for number in array:
            if number in current_node.children:
                self.sum += current_node.children[number].amount
                current_node.children[number].amount += 1
            else:
                current_node.children[number] = self.Node()
            current_node = current_node.children[number]

tree = Tree()
n = int(input())
for _ in range(n):
    input()
    tree.add(input().split())

print(tree.sum)
