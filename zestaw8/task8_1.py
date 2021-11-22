def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == b == 0 : 
        # c!=0
        if c!=0 : raise ValueError(f'Non zero value is not zero! {c} != 0')
        # 0 = 0
        else : return "0 = 0"
    elif a==0 or b==0 :
        if a == 0 : return f'y = {-c} / {b}'
        if b == 0 : return f'x = {-c} / {a}'
    else :
        if -c < 0 : return f'y = ({-a}x{-c}) / {b}' if c!=0 else f'y = {-a}x / {b}'
        else : return f'y = ({-a}x + {-c}) / {b}' if c!=0 else f'y = {-a}x / {b}'

print(solve1(0,0,0))

print(solve1(1,0,0))
print(solve1(1,0,4))

print(solve1(0,2,0))
print(solve1(0,2,4))

print(solve1(1,1,0))
print(solve1(1,1,1))
print(solve1(1,2,2))

#print(solve1(0,0,3))
            
    