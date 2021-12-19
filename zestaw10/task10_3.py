class Stack :
    def __init__(self) :
        self.data = []
        self.top = -1

    def pop(self) : 
        if(not self.isEmpty()) : 
            output = self.data[self.top]
            self.top -= 1
            return output
        else : 
            print(f'Stack is empty!')
            return None

    def isEmpty(self) :
        return True if(self.top == -1) else False

    def sizeof(self) :
        return len(self.data)

    def push(self, value) :
        if(self.data.count(value) == 0 or self.isEmpty()) :
            if(value >= 0 and value<= self.sizeof()) :
                self.data.append(value)
        
                self.top += 1    

    def peek(self) :
        if(not self.isEmpty()) :
            return self.data[self.top]
        else : 
            print(f'Stack is empty!')
            return None

    def str(self) :
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
    s.push(0)
    s.push(1)

    print(s.str())

    s.push(3)
    s.push(0)

    print(s.str())

    s.pop()

    print(s.str())
    print(s.isEmpty())


