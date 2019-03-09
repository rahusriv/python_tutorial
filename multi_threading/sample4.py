import threading
import timeit

def addlist( list1, list2, result, index ):
    #Add index
    result[index] = list1[index] + list2[index]

def createthread(list1, list2, result, index):
    download_thread = threading.Thread(target=addlist, args=(list1, list2, result, index))
    download_thread.start()

start = timeit.default_timer()
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]
list3 = [0,0,0,0,0,0,0,0,0,0]

for i in range(0,10):
    createthread(list1,list2,list3,i)
    #addlist(list1, list2, list3,i)

print(list3)
stop = timeit.default_timer()
print('Time: ', stop - start)