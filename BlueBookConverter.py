# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:15:58 2018

@author: 9V72n
青い本Converter
"""
import re
import os
file = open("importfile.txt", 'r')
file2 = open("temporaryfile.txt", 'w')  
texts = file.readlines()
count = 0
for text in texts:
    c = 0
    arrowcount = 0
    plaintext = text.replace('\n','')   
    matchObj = re.search("^(?![②-⑩]).+?」|.+?①.+?」", plaintext)
    matchObj2 = re.findall(">[②-⑩].+?」", plaintext)
    matchObj3 = re.search("②.+?」", plaintext)
    exception = re.search("have \[throw\] a conniption",plaintext)
    splittexts = re.split('[①-⑩]', plaintext)
    index = re.search(".+\|",plaintext)
    for text2 in splittexts:
        countnum = text2.count("¶")
        if countnum != 0:
            c += 1
        if countnum != 0:
            if exception:
                countnum -= 1
            for i in range(countnum):
                arrowcount = matchObj.group().count("→")
                if matchObj3 and arrowcount > 0:
                    count += 1
                    file2.write("{0} {1}\n".format(index.group(),matchObj3.group()))
                    print(count)
                if matchObj and c == 1 and arrowcount == 0:
                    count += 1
                    file2.write("{}\n".format(matchObj.group()))
                    print(count)
                if matchObj2 and c > 1:
                    count += 1
                    matchObj4 = matchObj2[c-2]
                    file2.write("{0} {1}\n".format(index.group(),matchObj4[1:]))
                    print(count)
file.close()
file2.close()
file3 = open("temporaryfile.txt", 'r') 
file4 = open("exportfile.txt", 'w') 
includehtml = file3.read()
deletehtml = includehtml.replace("<br><br>","")
file4.write(deletehtml)
file3.close()
file4.close()
os.remove("temporaryfile.txt")
input("Press any key to exit.")
