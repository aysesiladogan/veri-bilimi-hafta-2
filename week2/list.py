list = [12, 4, 9, 25, 30, 7, 18]

average = sum(list) / len(list)
biggests = [x for x in list if x > average]
print("Average: ", average)
print("Biggests: ", biggests)