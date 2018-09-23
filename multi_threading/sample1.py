#Download file using multi threading

import threading
import requests
import timeit

def download(link, filelocation):
    r = requests.get(link, stream=True)
    with open(filelocation, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

def createNewDownloadThread(link, filelocation):
    download_thread = threading.Thread(target=download, args=(link,filelocation))
    download_thread.start()

start = timeit.default_timer()

for i in range(0,100):
    file = "test" + str(i) + ".png"
    print(file)
    #download("http://stackoverflow.com/users/flair/2374517.png", file)
    createNewDownloadThread("http://stackoverflow.com/users/flair/2374517.png", file)

stop = timeit.default_timer()
print('Time: ', stop - start)