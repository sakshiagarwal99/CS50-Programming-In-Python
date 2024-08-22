def main():
    user_input = input("")
    slowdown(user_input)

def slowdown(u):
    print(u.strip().replace(" ","..."))

main()
