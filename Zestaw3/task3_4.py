while True:
    try:
        var = input()

        if var == "stop" : break

        x = float(var)

        print(f'{x} -> {x**3}')
    except Exception as e:
        print(e)

        print("Try again")

        pass