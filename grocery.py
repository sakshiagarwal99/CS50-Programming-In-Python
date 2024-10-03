def main():
    grocery_dict = {}
    while True:
        try:
            grocery_item = input("").strip().upper()
            if grocery_item in grocery_dict:
                grocery_dict[grocery_item] += 1
            else:
                grocery_dict[grocery_item] = 1
        except EOFError:
            break
    for item in sorted(grocery_dict):
        print(f"{grocery_dict[item]} {item}")

main()
