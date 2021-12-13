class RandomQueue:

    def __init__(self, size): 
        self.data = []
        self.numOfElem = 0
        self.size = size

    def insert(self, item): 
        if item != None and ( self.numOfElem < self.size ) :
            self.data.append(item)
            self.numOfElem += 1

    def remove(self) : # zwraca losowy element
        import random as r
        
        index = r.randint(0, self.numOfElem)

        removed = self.data[index]
        self.data[index] = None
        self.numOfElem -= 1

        self.resize()

        return removed

    def isEmpty(self) :
        return self.numOfElem == 0

    def is_full(self) : 
        return self.numOfElem == self.size

    def resize(self) :
        new_array = []

        for j in self.data : 
            if j != None : new_array.append(j)

        self.data = new_array    
    
    def clear(self) : # czyszczenie listy
        self.data = []

    def str(self) :
        o = ''
        for i in self.data : o += str(i);o += ', '
        
        return o[:-2]

if __name__ == '__main__' :
    r = RandomQueue(5)

    print(r.isEmpty())

    r.insert(12)
    print(r.isEmpty())
    r.insert(11)
    r.insert(10)
    r.insert(9)
    
    print(r.str())

    r.insert(8)

    print(r.str())
    print(r.is_full())

    r.remove()
    print(r.str())

    r.remove()
    print(r.str())

