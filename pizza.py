import sys
import csv
import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many comman-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    file = sys.argv[1]
    print(pizza(file))

def pizza(file):
    try:
        with open(file,"r") as p_file:
            reader = csv.DictReader(p_file)
            return tabulate.tabulate(reader,headers="keys",tablefmt = "grid")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()


