"""
Task2.4(5)
open file from input
and output frequencies 
"""

#define var
cnt = 0           #counter
flist = []        #file list
linked_file = ""  #linked file
ifile = ""        #input file data
splited_file = [] #splited file
taged_file = []   #taged file
f = ""            #filename
dic = {}          #dictionary

import os.path
import nltk

#loop
while True:
    #import data
    cnt += 1
    ifile = input("please inputfile" + str(cnt) + "(e to end input / q to quit) : ")

    #escape from loop
    if ifile == "e":
        break

    elif ifile == "q":
        quit()

    #file check    
    if os.path.isfile(ifile):
        #list.append
        flist.append(ifile)
        
    else:
        print("error : file does not exit")
        cnt -= 1
        
#link file
for i in flist:
    #open file
    f = open(i,"r")

    #load and link file
    linked_file += f.read()
    
    #close file
    f.close

#split file
splited_file = nltk.word_tokenize(linked_file)


#register dictionary
for i in splited_file:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

#sort and output
for key , value in sorted(dic.items() , key = lambda x:(x[1],x[0]) , reverse = True ):
    print(str(value) + "  " + key)

