import os
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    file = sys.argv[1]
    print(lines_of_code(file))

def lines_of_code(file):
    if os.path.isfile(file):
        with open(file,"r") as l_file:
            count = 0
            for line in l_file:
                stripped_line = line.strip()
                if stripped_line.startswith("# ") or stripped_line == "":
                    continue

                count = count + 1

            return count

    else:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
