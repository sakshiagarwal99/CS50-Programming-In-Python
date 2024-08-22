def main():
    user_input = input("")
    convert(user_input)

def convert(u):
    u = u.replace(":)",u"\U0001F642")
    u = u.replace(":(",u"\U0001F641")
    print(u)

main()

