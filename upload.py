# -*- coding: utf-8 -*-
import ftplib

class Upload:
    def __init__(host, user, password):
        __host = host
        __user = user
        __password = password

    def upload(file):
        ftp = ftplib.FTP(__host)
        ftp.set_pasv("true")
        ftp.login(__user, __password)

        for f in file:
            fp = open(file, 'rb')
            ftp.storbinary("STOR /sample/test.csv",fp)
            fp.close()

        ftp.close()