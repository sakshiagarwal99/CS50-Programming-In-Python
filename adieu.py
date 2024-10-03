import inflect
import sys
def main():
    names = []
    p = inflect.engine()
    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
            continue
        except EOFError:
            if names:
                print("\nAdieu, adieu, to " + p.join(names))
            sys.exit()

main()


