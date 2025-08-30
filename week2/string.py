sentence = input("Please enter a sentence: ")
words = sentence.split()
new_sentence = ' '.join([word.capitalize() for word in words])

print("Transformed sentence:", new_sentence)