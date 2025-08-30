n = int(input("How many reviews will you enter? "))

reviews = []
for i in range(n):
    review = input(f"Enter review {i+1}: ")
    reviews.append(review)

lengths = [len(r) for r in reviews]

good_count = sum(["good" in r.lower() for r in reviews])

longest_review = max(reviews, key=len)
shortest_review = min(reviews, key=len)

average_length = sum(lengths) / len(reviews)

print("Analysis Results:")
print("Total number of reviews:", len(reviews))
print('Number of reviews containing "good":', good_count)
print("Longest review:", longest_review)
print("Shortest review:", shortest_review)
print("Average length:", round(average_length, 1), "characters")
