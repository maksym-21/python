# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. 
# Chcemy zbudować napis z trzycyfrowych bloków, 
# gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami,
#  np. 007, 024. Wskazówka: str.zfill().

L = [1, 22, 333, 0,57]
O = []
for i in L:
    if(len(str(i)) < 3) :
        var = str(i).zfill(3)
        O.append(int(var))
    else : O.append(i)

print(O)