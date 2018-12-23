myfile = open("location.txt","r")

location_list = myfile.readlines()

print(location_list)

location_list_clean = []

for location in location_list:
    tmp = location.rstrip().upper()
    location_list_clean.append(tmp)
    #print(tmp)

print(location_list_clean)
input_location = input("Please enter your location : ")

if input_location.strip().upper() in location_list_clean:
    print("Location is correct. We will deliver your order")
else:
    print("Location incorrect . Can't deliver your order")
