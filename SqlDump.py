#!/usr/bin/env python
#coding:utf-8 
# --*-- encoding:utf-8 --*--

'''
Created on 2013-10-13

@author: poorevil
'''
import json,sys,linecache,time

def loadSourceFile(sourceFilePath):

    begin = time.time()

    lineCount = len(linecache.getlines(sourceFilePath))
    
    print lineCount
    
    kAmountPerThread = 800
    
    count = lineCount/kAmountPerThread + lineCount%kAmountPerThread
    print count
    
    for i in range(0,count+1):
        startOffset = i*kAmountPerThread + 1    #start with 1
        endOffset = (i+1)*kAmountPerThread
        if endOffset > lineCount:
            endOffset = lineCount

#        print '%d---%d'%(startOffset,endOffset)
        
        for offset in range(startOffset,endOffset+1):
#            print linecache.getline(sourceFilePath, offset)

            jsonDict = json.loads(linecache.getline(sourceFilePath, offset))
            print jsonDict['devieModel'],jsonDict['mobileImsi']
        
        if i > 50:
            break
    
    
    print (time.time() - begin)
    
    
#def wirteFile(sourceFilePath):
#    f = open('test.txt','w');
#    
#    str = '''{"devieModel":"SCH-I959","mobileImsi":"460030237321185"}\n'''
#    
#    for i in range(0,10000000):
#        f.write(str)
#    


if __name__ == '__main__': 
    sourceFilePath = sys.argv[1];
    loadSourceFile('test.txt')#(sourceFilePath)

#    wirteFile(sourceFilePath)
