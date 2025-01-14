# m a d a m

def palin(s):
    s = s.lower()
    if len(s) <= 1:
        print("Palindrome")
    else:
        if s[0] == s[-1]:
            palin(s[1:-1])
        else:
            print("Not a Palindrome")

palin("Nitin")
palin("madam")
palin("abba")
palin("python")
        

