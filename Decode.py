#!/usr/bin/env python
#coding:utf-8 
# --*-- encoding:utf-8 --*--

'''
Created on 2013年10月15日

@author: hanchao
'''

import base64,zlib,gzip,cStringIO
import zipfile

def main():
    b64Str = 'UEsDBBQACAgIAA+3/0IAAAAAAAAAAAAAAAABAAAAMD1Ru07DMBT9lchzlPiVtM7C0AWGdqrEwuLElhqIkyh1WlUICQYk+gkVAnWnrAgVBD9TEvEX2E2Lp3vO8bk6995rEBfF1YgrCSLQfjw0z3e7z3Wz/AYuqKvMkBOty8j357z0ElVJLrykUH5qK3+uMj/zp1KfF5UY5Nq7nJYneSouagiJoIjQPkM9i3AYH2nMEMG0I5MjSWgIMaO9oON1x8IOzQ4QHUyqg0MSUAghMlHLKk3sBAh70MBkwkstq8NYjnntZvNz/9quvn4f33bvy/Zl7TjNats83ZrvqojTTI5qZTsEiEFGKIJ9owg5S+WwENJu4nQ8cMYB7ut/y5mapkYw2SHe21DIKDOyzHXFcxuJmCZcmwKRnvHigKEQBS6I68WcL0AEXaAXpdXd/SlSAaJuQzd/UEsHCIfKf2Y0AQAAnAEAAA=='
    
    fp = open('aaa.zip','w')
    fp.write(base64.decodestring(b64Str))
    fp.close()
    
#     myzip=zipfile.ZipFile('aaa.zip') 
#     myfilelist=myzip.namelist() 
#     print myfilelist
    
#     data =  bytearray(base64.decodestring(b64Str))
# 
#     print zlib.decompress(base64.decodestring(b64Str),16+zlib.MAX_WBITS)

    decompress = zlib.decompressobj()
    print decompress.decompress(base64.decodestring(b64Str))
    
#     print gzip.GzipFile('0', 'rb', 9, cStringIO.StringIO(data)).read()

if __name__ == '__main__':
    main()



