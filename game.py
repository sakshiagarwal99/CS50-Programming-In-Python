import random

def valid_input(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except (ValueError,TypeError):
            pass


def main():
    level = valid_input("Level: ")
    random_number = random.randint(1, level)
    guess(random_number)

def guess(r):
    while True:
        g = valid_input("Guess: ")
        if g < r:
            print("Too small!")
        elif g > r:
            print("Too large!")
        elif g == r:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
