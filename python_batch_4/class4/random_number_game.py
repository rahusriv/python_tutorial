import random

random_num = random.randint(1,5)

#print(random_num)

num = int(input("Enter a number between 1 to 5"))

if(num==random_num):
    print("You guessed correctly you won")
    print("Random number = {}".format(random_num))
else:
    print("Sorry you lost , try again nect time !")
    print("Random number = {}".format(random_num))