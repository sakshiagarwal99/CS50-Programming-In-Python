def main():
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    with_vowel = input("Input: ")
    without_vowel = [letter for letter in with_vowel if letter not in vowels]
    print("Output:", ''.join(without_vowel))

main()
