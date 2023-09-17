class Node:
        def __init__(self, value):
            self.parent = None
            self.left = None
            self.right = None
            self.value = value


class Tree:
    def __init__(self, n):
        # Ключи - значения в уздах дерева, значения - ссылки на узлы
        self.tree_array = [''] + [ Node(i) for i in range(1, n + 1) ]
        self.tree_array[0] = self.tree_array[1]

        for i in range(2, n + 1):
            node = self.tree_array[i]
            parent = self.tree_array[i // 2]
            node.parent = parent
            if node.value % 2 == 0:
                node.parent.left = node
            else:
                node.parent.right = node

    # Вывод дерева
    def print(self):
        self.f(self.tree_array[0])

    def f(self, node):
        if node.left:
            self.f(node.left)

        print(node.value, end=' ')

        if node.right:
            self.f(node.right)

    # Поменять узел местами с родителем
    # v - узел
    # p - родитель
    # pp - родитель родителя
    def change(self, value):
        v = self.tree_array[value]
        p = v.parent
        left = False
        if p:
            pp = p.parent
            if pp and pp.left == p:
                left = True
        else:
            pp = None


        # Если v - корень
        if not p:
            return

        # Если v - левый потомок
        if v.parent.left == v:
            v_left_child = v.left

            v.parent = pp
            if pp:
                if left:
                    pp.left = v
                else:
                    pp.right = v
                 
            else:
                self.tree_array[0] = v

            v.left = p
            p.parent = v

            p.left = v_left_child
            if v_left_child:
                v_left_child.parent = p

        # Если v - правый потомок
        elif v.parent.right == v:
            v_right_child = v.right

            v.parent = pp
            if pp:
                if left:
                    pp.left = v
                else:
                    pp.right = v
            else:
                self.tree_array[0] = v

            v.right = p
            p.parent = v

            p.right = v_right_child
            if v_right_child:
                v_right_child.parent = p
        

n, q = map(int, input().split())

tree = Tree(n)

for number in input().split():
    tree.change(int(number))

tree.print()
