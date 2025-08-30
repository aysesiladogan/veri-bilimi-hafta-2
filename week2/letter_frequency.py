letter = input("Enter a letter: ").lower()

frequency = {}

for char in letter:
    if char in letter:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print(frequency)                