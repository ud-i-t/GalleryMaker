# coding: SHIFT-JIS
import lxml.html
import requests
import codecs

for st in range(1,200):
    target_url = "http://big2.dip.jp/cgi-bin/diary.cgi?start="+str(st*8)+"&pass="
    r = requests.get(target_url)
    r.encoding = "shift-jis"
    target_html =r.text
    root = lxml.html.fromstring(target_html)

    #print(target_html)

    fout = codecs.open('drklab_'+str(st)+'.html', 'w', 'utf-8')
    fout.write(target_html)
    fout.close()
