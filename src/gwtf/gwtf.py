import os
import linecache

with open('temp.tmp') as f:
    tempdata = f.read()

with open('wallpath.txt', "w") as f:
    for line in tempdata:
        line = line.strip()
    f.write(tempdata)
    f.close()

os.remove('temp.tmp')

# extracting the 5th line
wallpath = linecache.getline('wallpath.txt', 3)
new_wallpath = wallpath.replace('WallPaper    : ', '')
with open('wallpath.txt','r') as f:
    replace = ""
    for line in tempdata:
        line = line.strip()
    f.close()

    # opening the file in write mode
    with open('wallpath.txt', "w") as f:
        f.write(new_wallpath)
        f.close()
    #f.write()

print(new_wallpath)

quit()