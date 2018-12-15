myfile = open("location.txt","r")

location_list = myfile.readlines()
list_of_list = []
for i in range(1,101):
    myfile = open("location.txt".format(i),"r")
    file_list = myfile.readlines()
    list_of_list.append(file_list)
