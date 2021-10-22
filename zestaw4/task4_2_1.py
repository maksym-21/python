def make_ruler(arg) :
    text = "|"
    numbers = "0"

    length = int(arg)

    for i in range(length) :
        text += "....|"
        numbers += str(i+1).rjust(5)

    return f'{text}\n{numbers}'

print(make_ruler(4))