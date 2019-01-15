def putInfoToDict(fileName):
    retDict = {}
    with open(r'e:/file001.txt') as f:
        lines = f.read().splitlines()

        for line in lines:
            line = line.replace('(', '').replace(')', '').replace(';', '').strip()

            parts = line.split(',')
            ciTime = parts[0].strip().replace("'", '')
            lessonid = int(parts[1].strip())

            userid = int(parts[2].strip())

            toAdd = {'lessonid': lessonid, 'checkintime': ciTime}
            # if not in, need to create list first
            if userid not in retDict:
                retDict[userid] = []
            retDict[userid].append(toAdd)

    return retDict
ret = putInfoToDict('file001.txt')
import pprint
pprint.pprint(ret)