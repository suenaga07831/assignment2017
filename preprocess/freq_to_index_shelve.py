"""
Task2.4(7)
open file from input
next, peform indexing.
finally , describe saving object to disk
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
apdic = {}        #dictionary value is appearance
save_file = ""    #save file
shdic = {}        #shelve dictionary

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


#counter reset
cnt = 0

#register dictionary sorted by appearance
for i in splited_file:
    if i in apdic:
        continue
    else:
        cnt += 1
        apdic[i] = cnt
        

#import shelve and save destination file
import shelve
save_file = input("please save destination : ")

#open save file
shdic = shelve.open(save_file)


#register dictionary
for key , value in sorted(apdic.items() , key = lambda x:x[1]):
    shdic[key] = value
    
#check save file
if os.path.isfile(save_file):
    print("file save ok .")
else:
    print("error : missed save .")
    
#close save file    
shdic.close()




