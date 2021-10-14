height = int(input("pls give me a height:"))
width = int(input("pls give me a width:"))

result = ""
row = "+---" * (width) + '+'

for i in range(height):
    result += row + '\n'
    result += "|   " * (width) + '|\n'

result += row + '\n'

print(result)