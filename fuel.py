def main():
    fuel = howfull()
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def howfull():
    while True:
        try:
            x, y = map(int, input("Fraction: ").split("/"))

            if y == 0 or x > y:
                continue

            return round((x/y) * 100)
        except (ValueError,ZeroDivisionError):
            continue

main()


