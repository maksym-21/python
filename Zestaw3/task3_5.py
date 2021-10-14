print("pls give me a length:")

var = input()
length = int(var)

text = "|"
numbers = "0"

for i in range(length) :
    text += "....|"

    numbers += str(i+1).rjust(5)

print(f'{text}\n{numbers}')