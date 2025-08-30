letter = input("Enter a letter: ")

if letter == letter[::-1]:
    print(letter, "is a palindrome")
else:
    print(letter, "is not a palindrome")