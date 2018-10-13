#and/or opretations

statement1 = input("Whats your first statement ? ")
statement2 = input("Whats your second statement ? ")
word = input("What word you want to find ? ")

if( (word in statement1) and (word in statement2)):
    print("Word exists in both the statements")
elif((word in statement1) or (word in statement2)):
    print("Word exists in one of the statements")
else:
    print("Word does not eist in any statement")
