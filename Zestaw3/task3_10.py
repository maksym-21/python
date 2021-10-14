def function(number:str):
    if number == "" : return 0

    map = { 'M' : 1000, 'D' : 500,  'C' : 100 , 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

    value = [map[j] for j in number]

    return sum(
        val if val >= next_val else -val
        for val, next_val in zip(value[:-1], value[1:])
    ) + value[-1]

print(function("XXII"))
print(function(""))