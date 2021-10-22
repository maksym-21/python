def make_grid(height:int, width:int) :
    result = ""
    row = "+---" * (width) + '+'

    for i in range(height):
        result += row + '\n'
        result += "|   " * (width) + '|\n'

    result += row + '\n'

    return result

print(make_grid(5, 2))