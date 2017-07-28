# coding: UTF-8
import os
import sys
import codecs
from PIL import Image

filepath = "./gallery/thumb"
filelist = os.listdir(filepath)

string = ""

links = ""

filelist.reverse()

for d in filelist :
    links += '<li><a href="./gallery_' + d + '.html">' + d + '年</a></li>\r\n'

template = "./template/index.html"
findex = codecs.open(template,'r', "UTF-8")
string = findex.read()
string = string.replace("[year_link]", links)
findex.close()

fout = codecs.open('./gallery/index.html', 'w', 'utf-8')
fout.write(string)
fout.close()
    
    
for d in filelist :
    tags = ["", "", ""]
    heights = [0, 0 ,0];

    dirlist = os.listdir(filepath + "/" + d)
    for f in dirlist :
        img = Image.open(filepath + "/" + d + "/" + f, 'r')

        # 高さ
        size = img.size
        minCol = heights.index(min(heights))
        tags[minCol] += '<a href="./img/' + d + '/' + f + '"><img src="thumb/' + d + '/' + f + '"></a>\r\n'
        heights[minCol] += size[1]
        

    template = "./template/gallery.html"
    f = codecs.open(template,'r', "UTF-8")
    string = f.read()
    f.close()
    
    for i in range(0,3):
        string = string.replace("[pictures_" + str(i+1) + "]", tags[i])

    print(string)
    fout = codecs.open('./gallery/gallery_' + d + '.html', 'w', 'utf-8')
    fout.write(string)

    fout.close()

