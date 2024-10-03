import random

def main():
    level = get_level()
    score = 0
    count = 10
    for _ in range(count):
        x, y = generate_integer(level)
        error = 3
        while error > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score = score + 1
                    break
                else:
                    print("EEE")
                    error = error - 1
            except (ValueError,TypeError):
                print("EEE")
                error = error - 1

        if error == 0:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except (ValueError, TypeError):
            pass


def generate_integer(level):
    if level == 1:
        lower = 0
        upper = 9
    else:
        lower = 10**(level - 1)
        upper = (10**level) - 1
    x = random.randint(lower,upper)
    y = random.randint(lower,upper)
    return x,y

if __name__ == "__main__":
    main()
