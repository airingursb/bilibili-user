# -*-coding:utf8-*-

import urllib
import re

f = open("/Users/airing/Documents/work/Data/bilibili_user_face.txt")
line = f.readline()
for i in range(1, 1000):
    print line,
    if re.match('http://static.*', line):
        line = f.readline()
        print 'noface:' + str(i)
    else:
        path = r"/Users/airing/Documents/work/Data/face/" + str(i) + ".jpg"
        data = urllib.urlretrieve(line, path)
        line = f.readline()
        print 'succeed:' + str(i)

f.close()

