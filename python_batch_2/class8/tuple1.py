
song1 = "Welcome to the night","Alice Cooper",1997,10000,"Hip Hop","English"
song2 = "This is the time","Metallica",1980,5000,"Rock","English"
song3 = "Manmarziya ","Arijith Singh", 2018,4000,"Blues","Hindi"

list_songs = []
list_songs.append(song1)
list_songs.append(song2)
list_songs.append(song3)
#song1[4] = list2
print(list_songs)

for song in list_songs:
    name,artist,year,copies_sold,genre,language = song
    print("{} , {} , {} , {} , {} , {}".format(name,artist,year,copies_sold,genre,language))

#print("Name of the song is {}".format(song1[0]))
#song1 = ("It all starts now",10)
#print(song1)

