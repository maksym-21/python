class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f'Node(name->{self.data})'

class List:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, other):
        if self.head == None : 
            self.head = other
            self.last = self.head
        else :
            t = self.last
            t.next = other
            self.last = other  

    def search(self, data): # klasy O(n)
        k = None
        
        if self.head.next == None : return self.head if data == self.head.data else None
        elif self.last.data == data : return self.last
        else :
            k = self.head
            while k.next != None :
                if k.data == data : return k
                
                k = k.next

        return None

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

    def reverse(self):
        prev = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev 

        return self.__str__()

    def __str__(self) -> str:
        out = ''
        s = self.head

        out += f'{s.__str__()}\n'
        while s.next != None :
            out += s.next.__str__()
            out += '\n'
            s = s.next

        return out

if __name__ == '__main__' :
    L = List()

    L.add(Node(5))
    L.add(Node(3))
    L.add(Node(2))
    L.add(Node(22))

    print()
    print(L.__str__())

    print()
    print(L.search(2))    
    
    print()
    print(L.find_min())
    print(L.find_max())

    print()
    print(L.reverse())  