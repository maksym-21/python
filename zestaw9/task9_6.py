class Node:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def count_leafs(top) : 
    if top is None : return 0
    elif top.left is None and top.right is None : return 1
    else : return count_leafs(top.left) + count_leafs(top.right)

def count_total(top) :
    if top is None : return 0
    elif top.right is None and top.left is None : return 1
    else : return 1 + count_total(top.right) + count_total(top.left)

def calc_total(top) -> int :
    if top is None : return 0
    elif top.right is None and top.left is None : return top.data
    else : return top.data + calc_total(top.left) + calc_total(top.right)

if __name__ == '__main__' :
    main = Node(4)

    main.left = Node(1)
    main.right = Node(1)

    main.left.left = Node(1)
    main.left.right = Node(1)
    main.right.right = Node(1)
    main.right.left = Node(1)

    print(calc_total(main))
    print(count_total(main))
    print(count_leafs(main))


