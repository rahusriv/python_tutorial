import random

lucky_draw = ["car", "shoes", "bike", "mobile", "television", "ear phones"]

len_list = len(lucky_draw)

ind = random.randint(0,len_list)

print("Congrats you have won a {}".format(lucky_draw[ind]))