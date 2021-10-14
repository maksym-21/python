# Czy podany kod jest poprawny składniowo w Pythonie? 
# Jeśli nie, to dlaczego?

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# 1 -> składniowo poprawny

# for i in "qwerty": if ord(i) < 100: print (i)
# 2 -> niepoprawny (syntaxerror ,zadużo zdań w 1 linijce kodu)

# for i in "axby": print (ord(i) if ord(i) < 100 else i)
# 3 -> składniowo poprawny