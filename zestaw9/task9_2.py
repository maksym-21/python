class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f'Node(name->{self.data})'    

class SingleList:
    def __init__(self, name:str) :
        self.name = name
        self.head = None
        self.last = None

    def add(self, other:Node) :
        if self.head == None : 
            self.head = other
            self.last = self.head
        else :
            t = self.last
            t.next = other
            self.last = other

    def __str__(self) -> str:
        output = f'List :  name -> {self.name}, head -> {self.head}\n'

        if self.last != self.head :
            k = self.head
            odrer = 1
            while self.last.next != k.next :
                k = k.next
                output += f'\tnode nr{odrer} -> {k.__str__()}, '
                output += f'next -> {k.next}\n'
                odrer+=1
            
            return output    
        else : return output

    def search(self, data): # klasy O(n)
        k = None
        
        if self.last == self.head : return self.head if data == self.head.data else False
        else :
            k = self.head
            while self.last != k :
                if k.data == data : return k
                
                k = k.next

            return None if k.data != data else k
                
    def find_min(self) : # klasy O(n)
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        min = float('inf')

        if self.last == self.head : return self.head.data
        else :
            k = self.head
            if min > k.data : min = k.data
            while self.last.next != k.next :
                if min > k.data : min = k.data

                k = k.next

            return min if self.last.data > min else self.last.data

    def find_max(self) : # klasy O(n)
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        max = float('-inf')

        if self.last == self.head : return self.head.data
        else :
            k = self.head
            if max < k.data : max = k.data
            while self.last.next != k.next :
                if max < k.data : max = k.data

                k = k.next

            return max if self.last.data < max else self.last.data

    def reverse(self) : # klasy O(n)
        # Odwracanie kolejności węzłów na liście.
        arr = []
        k = self.head
        while self.last.next != k.next :
            arr.append(k.data)

            k = k.next
        arr.append(k.data)
        
        ar = arr[::-1]
        print(ar)

        L_new = SingleList(self.name)

        for i in ar :
            L_new.add(Node(i))

        return L_new    
    

if __name__ == '__main__' :
    L = SingleList('my_list')

    L.add(Node(5))
    L.add(Node(3))
    L.add(Node(2))
    L.add(Node(22))

    print(L.search(2))    
    print(L.find_min())
    print(L.find_max())
    
    print(L.__str__())
    print(L.reverse())



