class Node:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self,other) :
        self.parent = other

    def count_leafs(self,top) : 
        if top is None : return 0
        elif top.left is None and top.right is None : return 1
        else : return self.count_leafs(top.left) + self.count_leafs(top.right)

    def count_total(self,top) :
        if top is None : return 0
        elif top.right is None and top.left is None : return 1
        else : return 1 + self.count_total(top.right) + self.count_total(top.left)

    def calc_total(self,top) -> int :
        if top is None : return 0
        elif top.right is None and top.left is None : return top.data
        else : return top.data + self.calc_total(top.left) + self.calc_total(top.right)

if __name__ == '__main__' :
    main = Node(4)

    main.left = Node(1)
    main.right = Node(1)

    main.left.left = Node(1)
    main.left.right = Node(1)
    main.right.right = Node(1)
    main.right.left = Node(1)


    binary = BinaryTree(main)

    print(binary.calc_total(main))
    print(binary.count_total(main))
    print(binary.count_leafs(main))


