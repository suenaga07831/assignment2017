"""
Task2.5(1)
open directory from input

"""

#define var
cnt = 0           #counter
file_list = []    #file list
linked_file = ""  #linked file
splited_file = [] #splited file
f = ""            #filename
dic = {}          #dictionary
save_file = ""    #save file
output = ""       #info
shelf = ""        #shelve
shdic = {}        #shelve dictionary
bcdic = {}        #backup dictionary
bccnt = 0         #backup counter
imp_dir = ""      #imported directory

import os
import nltk
import sys

#import inputdata
args = sys.argv

#define dir
if len(args) == 2:
    imp_dir = args[1]

    if os.path.isdir(imp_dir) == False:
        print("error : directory does not exist")
        quit()

else:
    print("please write by this format")
    print("dir_to_fv.py <import directory>")
    quit()

#get file list
file_list = os.listdir(imp_dir)

#delete directory from file list
for i in file_list[:]:
    if os.path.isdir((imp_dir + i )):
        del file_list[cnt]
    else:
        cnt += 1
        
#link file
for i in file_list:
    #open file
    f = open((imp_dir + i),"r")

    #load and link file
    linked_file = f.read()
    
    #close file
    f.close

    #split file
    splited_file = nltk.word_tokenize(linked_file)

    #import shelve file
    import shelve
    save_file = "shelve.db"

    #open shelve file
    shelf = shelve.open(save_file)

    #import data
    #index
    if "index" in shelf:
        shdic = shelf["index"]
        bcdic = shelf["index"]

        #counter
    if "cnt" in shelf:
        cnt = shelf["cnt"]

    else:
        cnt = 0

    #register frequency in dictionary
    for j in splited_file:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1

    #delete words not appearing
    for j in list(shdic):
        if j in dic:
            continue
        else:
            del shdic[j]
        
    bccnt = len(shdic)

    #register appearance in dictionary
    for j in splited_file:
        if j in shdic:
            continue
        else:
            cnt += 1
            shdic[j] = cnt
        
    #load data
    output = ""
    for key , value in sorted(shdic.items() , key = lambda x:x[1] ):
        output += ( str(value) + ":" + str(dic[key]) + " ")

    #output and write
    print(output)

    #update shelves
    bcdic.update(shdic)

    shelf["index"] = bcdic
    shelf["cnt"] = cnt
    shelf[(imp_dir + i)] = shdic

    #close shelf
    shelf.close()
