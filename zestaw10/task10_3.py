class Stack :
    def __init__(self) :
        self.data = []
        self.top = -1

    def __pop__(self) : 
        if(not self.isEmpty()) : 
            output = self.data[self.top]
            self.top -= 1
            return output
        else : 
            print(f'Stack is empty!')
            return None

    def isEmpty(self) :
        return True if(self.top == -1) else False

    def __sizeof__(self) :
        return len(self.data)

    def __push__(self, value) :
        if(self.data.count(value) == 0 or self.isEmpty()) :
            if(value >= 0 and value<= self.__sizeof__()) :
                self.data.append(value)
        
                self.top += 1    

    def __peek__(self) :
        if(not self.isEmpty()) :
            return self.data[self.top]
        else : 
            print(f'Stack is empty!')
            return None

    def __str__(self) :
        output = ''

        if not self.isEmpty() : 
            for j in range(len(self.data)) : 
                if self.top >= j : 
                    output += str(self.data[j])
                    output += ' ,'

            output = output[:-1]
            output = output[::-1]

            return 'Stack -> ' + output
        else : return None

if __name__ == '__main__' :
    s = Stack()

    print(s.isEmpty())
    s.__push__(0)
    s.__push__(1)

    print(s.__str__())

    s.__push__(3)
    s.__push__(0)

    print(s.__str__())

    s.__pop__()

    print(s.__str__())
    print(s.isEmpty())


