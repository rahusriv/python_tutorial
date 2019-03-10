para = input("Enter a paragraph: ")
word = input("Which word you want to search? ")

word_stripped_lower = word.strip().lower()
para_lower = para.lower()

if (word_stripped_lower in para_lower):
    print("Your word found in the given paragraph")
else:
    print("Sorry no such word found in the given paragraph")