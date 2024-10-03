def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#start with 2 letters atleast
#min 2 char max 6 (numbers or letters)
#numbers not in middle, must come at end and cannot start with 0
#no periods, spaces, punctuation marks
def is_valid(s):
    if not is_length_valid(s):
        return False

    if not starts_with_two_letters(s):
        return False

    if not numbers_at_end(s):
        return False

    if not s.isalnum():
        return False

    return True

def is_length_valid(s):
    return 2 <= len(s) <= 6

def starts_with_two_letters(s):
    return s[0:2].isalpha()


def numbers_at_end(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if not s[i:].isdigit():
                return False
    return True


main()
