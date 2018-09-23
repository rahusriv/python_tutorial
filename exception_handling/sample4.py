import os
try:
    f = open("random_file.txt", 'r')
except OSError as err:
    print('cannot open file')
    print(err)
else:
    print("File random.txt", 'has', len(f.readlines()), 'lines')
    f.close()