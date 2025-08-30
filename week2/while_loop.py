sum = 0
piece = 1

while True:
    number = int(input("Enter a number (0 to stop): "))
    if number == 0:
        break
    sum += number
    piece += 1

if piece > 0:
    average = sum / piece
    print("Sum: ", sum) 
    print("Average: ", average)
else:
    print("No numbers were entered.")    