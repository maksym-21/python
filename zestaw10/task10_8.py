class RandomQueue:

    def __init__(self, size): 
        self.data = []
        self.numOfElem = 0
        self.size = size
        self.tail = -1

    def insert(self, item): 
        if item != None and self.size > self.numOfElem :
            self.data.append(item)
            self.numOfElem += 1
            self.tail += 1

    def remove(self) : # zwraca losowy element
        import random as r
        
        index = r.randint(0, self.numOfElem)
        
        tmp = self.data[index]
        tmp2 = self.data[self.tail]

        self.data[self.tail] = tmp

        self.data[index] = tmp2

        out = self.data.pop(self.tail)
        self.tail -= 1
        self.numOfElem -= 1

        return out

    def isEmpty(self) :
        return self.numOfElem == 0

    def is_full(self) : 
        return self.numOfElem == self.size

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

