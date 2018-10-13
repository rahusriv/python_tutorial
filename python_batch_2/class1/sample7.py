# Checking if a string is sub-string of another string

all_localities = "hsr, koramangala, bellandur, btm, mg road"
locality = input("Please enter your locality: ")

if locality in all_localities:
    print("Your locality exists in bangalore")
else:
    print("Your locality is not in bangalore")