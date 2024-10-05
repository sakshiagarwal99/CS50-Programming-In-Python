import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    read_file = sys.argv[1]
    write_file = sys.argv[2]
    readfrom(read_file,write_file)


def readfrom(read_file,write_file):
    try:
        students = []
        with open(read_file,"r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                house = row["house"]
                students.append({"first":first.strip(),"last":last.strip(),"house":house.strip()})

        with open(write_file,"a") as w_file:
            writer = csv.DictWriter(w_file, fieldnames=["first","last","house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"Could not read {read_file}")

if __name__ == "__main__":
    main()
