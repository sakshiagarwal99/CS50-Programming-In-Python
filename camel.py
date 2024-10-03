def main():
    camel_case = input("camelCase: ")
    print(f"snake_case: {snake_case(camel_case)}")

def snake_case(letters):
    snake = ""
    for letter in letters:
        if letter == letter.upper():
            snake += "_" + letter.lower()
        else:
            snake += letter
    return snake

main()
