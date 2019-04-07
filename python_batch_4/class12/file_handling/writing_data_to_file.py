
with open("/home/rahul/Desktop/fruits.txt","w") as myfile :

    myfile.write("mango\n")
    myfile.write("apple\n")
    fruit_list = []
    while(True):
        fruit = input("Enter a fruit (type 'exit' to end the loop)")
        if fruit == 'exit':
            break
        fruit = fruit + "\n"
        fruit_list.append(fruit)


    myfile.writelines(fruit_list)
