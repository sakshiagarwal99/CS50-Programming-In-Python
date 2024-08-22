def main():
    time = input("What time is it? ")
    converted_time = convert(time)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

def convert(time):
    if "a.m." in time or "p.m." in time:
        time, period = time.split()
        hour, minute = map(float, time.split(":"))

        if period == "p.m." and hour != 12.00:
            hour = hour + 12.00
        elif period == "a.m." and hour == 12.00:
            hour = 0.00

    else:
        hour, minute = map(float,time.split(":"))

    return hour + minute/60.00

if __name__ == "__main__":
    main()
