class Stack :
    def __init__(self, size = 10) :
        self.size = size
        self.items = size * [None]
        self.matrix = {}
        for j in range(size) :
            self.matrix[j] = 0
        self.n = 0
        self.top = -1

    def pop(self) : 
        if(not self.isEmpty()) : 
            output = self.items[self.top]
            
            self.items[self.top] = None
            self.matrix[output] = 0

            self.top -= 1
            self.n -= 1
            return output
        else : 
            print(f'Stack is empty!\n')
            return None

    def isEmpty(self) :
        return True if(self.top == -1) else False

    def sizeof(self) :
        return self.n if self.n > 0 else 0

    def push(self, value) :
        if (self.size >= value and value >= 0) :
            if(self.top + 1 <= self.size) :
                if(self.matrix[value] == 0) :
                    self.top += 1
                    self.items[self.top] = value

                    self.matrix[value] = 1

                    self.n += 1
                else : print(f'Value {value} is already in stack!\n')
            else : print('Stack is full!\n')
        else : print(f'Value {value} is not in [0, {self.size}] \n')

    def peek(self) :
        if(not self.isEmpty()) :
            return self.data[self.top]
        else : 
            print(f'Stack is empty!\n')
            return None

    def str(self) :
        output = ''

        if not self.isEmpty() : 
            for j in range(self.top + 1) : 
                output += str(self.items[j])
                output += ', '

            output = output[:-2]

            return 'Stack -> ' + output + '\n'
        else : return 'Stack is empty!\n'

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


