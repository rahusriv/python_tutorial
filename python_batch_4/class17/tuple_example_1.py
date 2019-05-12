song1 = ("welcome to the night", "Alice Cooper", 1987,["2 million", "HBO"])
song2 = ("My new song", "Artist 2", 2001,["1 million", "Sony"])


tuple_of_all_songs = (song1, song2)

for song in tuple_of_all_songs:
    name, artist, year, mylist = song
    print(name)
    print(artist)
    print(year)
    print(mylist)
    print(song)
    mylist[0] = "no copies sold"
    mylist[1] = "xyz"
    #mylist = ["no song sold", "xyz"]
    #song[3] = ["no song sold", "xyz"]
    print(song)
    print("*"*100)

#tmp_list = tuple_of_all_songs[0][3]
tuple_of_all_songs[0][3][0] = "*** no copies sold song 1"
tuple_of_all_songs[0][3][1] = "***xyz song 1"

#tmp_list = tuple_of_all_songs[1][3]
tuple_of_all_songs[1][3][0] = "*** no copies sold song 2"
tuple_of_all_songs[1][3][1] = "***xyz song 2"

print(tuple_of_all_songs)

