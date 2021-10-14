# L = [3, 5, 4] ; L = L.sort()
# L = none -> list.sort() sorts the list in place

# x, y = 1, 2, 3
# ValueError: too many values to unpack (expected 2), actual 3

# X = 1, 2, 3 ; X[1] = 4
# X is immutable, so you can not reinit X[i]

# X = [1, 2, 3] ; X[3] = 4
# IndexError: list X assignment index out of range

# X = "abc" ; X.append("d")
# AttributeError: 'str' object has no attribute 'append'

# L = list(map(pow, range(8)))
# pow() missing required argument 'exp' (pos 2) indicates 
# that our call is missing an argument at position 2. 
# The call must contain the second argument 
# which is named exp (short for "exponent").