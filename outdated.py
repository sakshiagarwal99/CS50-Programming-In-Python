def main():
    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = map(int, date.split("/"))

                if month < 1 or month > 12 or day < 1 or day > 31:
                    raise ValueError

                print(f"{year:04}-{month:02}-{day:02}")
                break

            elif "," in date:
                month_name, day, year = date.replace(",", "").split()
                day = int(day)
                year = int(year)

                if month_name not in months or day < 1 or day > 31:
                    raise ValueError

                month = months[month_name]

                print(f"{year:04}-{month}-{day:02}")
                break
            else:
                raise ValueError

        except (ValueError, IndexError):
            continue

main()
