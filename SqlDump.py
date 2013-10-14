#!/usr/bin/env python
#coding:utf-8 
# --*-- encoding:utf-8 --*--

'''
Created on 2013-10-13

@author: poorevil
'''
import json,sys,linecache,time

def loadSourceFile(sourceFilePath,targetFilePath):

    targetFile = open(targetFilePath,'w');

    begin = time.time()

    lineCount = len(linecache.getlines(sourceFilePath))
    
    print '源数据共：%d条'%lineCount
    
    kAmountPerThread = 800
    
    count = lineCount/kAmountPerThread + (lineCount%kAmountPerThread and 1 or 0)
    print '按每段800条数据拆分成 %d 段'%count
    
    for i in range(0,count+1):
        startOffset = i*kAmountPerThread + 1    #start with 1
        endOffset = (i+1)*kAmountPerThread
        if endOffset > lineCount:
            endOffset = lineCount

#        print '%d---%d'%(startOffset,endOffset)
        
        insertBeginStr = '''INSERT INTO `kld_device` (`id`, `device`, `imsi`) VALUES\n'''
        
        targetFile.write(insertBeginStr)
        
        '''INSERT INTO `kld_device` (`id`, `device`, `imsi`) VALUES
(null, "GoDonie","460023121305631"),
(null, "GoDonie","460023121305631");'''
        
#         print '%d    %d'%(startOffset,endOffset+1)
        for offset in range(startOffset,endOffset+1):

            jsonDict = json.loads(linecache.getline(sourceFilePath, offset))
#             print jsonDict['devieModel'],jsonDict['mobileImsi']
            
            targetFile.write('''(null, "%s","%s")'''%(jsonDict['devieModel'],jsonDict['mobileImsi']))
            
            if offset == (endOffset):
                targetFile.write(';\n')
            else:
                targetFile.write(',\n')
            
        
    print '总耗时：%f秒'%(time.time() - begin)
    
    targetFile.close()
    
    
def wirteFile(sourceFilePath):
    f = open('test.txt','w');
    
    str = '''{"devieModel":"SCH-I959","mobileImsi":"460030237321185"}\n'''
    
    for i in range(0,10000):
        f.write(str)
    
    f.close()


if __name__ == '__main__': 
    sourceFilePath = 'test.txt'  #sys.argv[1];
    targetFilePath = 'target.sql'  #sys.argv[2];
    loadSourceFile(sourceFilePath,targetFilePath)

#     wirteFile(sourceFilePath)
