import os
import sys
from mutagen.easyid3 import EasyID3
def getMp3FilesInDir(dir):
    if dir == "":
        dir= os.getcwd()

    files = os.listdir(dir)
    allMp3Files = []
    for file in files:
        if ".mp3" in file:
            allMp3Files.append(dir + "/" + file);
    dirsOnly = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
    for downDir in dirsOnly:
            allMp3Files.extend(getMp3FilesInDir(dir + "/" + downDir))
    return allMp3Files


if not len(sys.argv) == 2:
    print("Simple tool for recursive correction bad tag encryption (eg Áåëàÿ ÿáëûíÿ ãðîìó)")
    print("cp1251(windows-1251) -> utf-8")
    print("usage: python " +sys.argv[0] + " [directory] ")
    exit();

mp3Files = getMp3FilesInDir(sys.argv[1])
print(mp3Files)

i = 0;
atI = int(len(mp3Files)/10)+1
for fileName in mp3Files:
    try:
         tags = EasyID3(fileName)
    except:
        continue
    ids = ['artist' ,'title', 'album' ] #for more id apeend it
    for id in ids:
        try:
            newTag = (tags[id])[0].encode("latin-1").decode('cp1251').encode('utf-8').decode('utf-8')
        except:
            continue
        tags[id] = newTag
    tags.save()
    i += 1
    if i%(atI) == 0:
        print(str(i) + "/" + str(len(mp3Files)))
print ("done " + str(i))
