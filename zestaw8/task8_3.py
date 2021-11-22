import random as r

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    points_c = 0
    points_sq = 0

    for i in range(n**2) :
        # generate some x and y
        x = r.uniform(-1,1)
        y = r.uniform(-1,1)

        # if (x, y) lies inside the circle
        if x**2 + y**2 <= 1 : points_c += 1

        points_sq += 1

        pi = 4 * points_c / points_sq
    
    return pi

print(calc_pi(100))
print(calc_pi(140))
print(calc_pi(200))
print(calc_pi(300))
print(calc_pi(100))
