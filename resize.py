# coding: UTF-8
import os
import shutil
from PIL import Image

filepath = "./original"
filelist = os.listdir(filepath)

string = ""

i = 1;
for d in filelist :
        dirlist = os.listdir(filepath + "/" + d)
        if(os.path.exists("./gallery/img/" + d)):
                shutil.rmtree("./gallery/img/" + d)
        if(os.path.exists("./gallery/thumb/" + d)):
                shutil.rmtree("./gallery/thumb/" + d)
                
        os.mkdir("./gallery/img/" + d)
        os.mkdir("./gallery/thumb/" + d)
                
        for f in dirlist :
                img = Image.open(filepath + "/" + d + "/" + f, 'r')
                thumb = img
                if img.size[1] > 1200:
                   img.thumbnail((1200, 1200), Image.ANTIALIAS)     
                img.save("./gallery/img/" + d +"/" + str(i) + ".png", 'PNG', quality=100, optimize=True)

                #サムネ
                thumb.thumbnail((320, 320), Image.ANTIALIAS)
                thumb.save("./gallery/thumb/" + d +"/" + str(i) + ".png", 'PNG', quality=100, optimize=True)

                print("処理完了> ./gallery/thumb/" + d +"/" + str(i))
                i += 1
