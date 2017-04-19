"""
Task2.4(9)
open file from input
next, peform indexing.
finally output index and frequency sorted by index
"""

#define var
cnt = 0           #counter
flist = []        #file list
linked_file = ""  #linked file
ifile = ""        #input file data
wfile = ""        #write file 
splited_file = [] #splited file
taged_file = []   #taged file
f = ""            #filename
dic = {}          #dictionary
apdic = {}        #dictionary value is appearance
save_file = ""    #save file
write_file = ""   #write file(adress)
output = ""       #info
shelf = ""        #shelve
shdic = {}        #shelve dictionary
bcdic = {}        #backup dictionary
bccnt = 0         #backup counter

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
        #update write file
        write_file = "bow_" + ifile
        
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

#import shelve file
import shelve
save_file = input("please shelve file : ")

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
for i in splited_file:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

#delete words not appearing
for i in list(shdic):
    if i in dic:
        continue
    else:
        del shdic[i]
        
bccnt = len(shdic)
        
#register appearance in dictionary
for i in splited_file:
    if i in shdic:
        continue
    else:
        cnt += 1
        shdic[i] = cnt
        
#open write file
if write_file == "":
    write_file = "shelve.db"

wfile = open( write_file , "w")

#load data
for key , value in sorted(shdic.items() , key = lambda x:x[1] ):
    output += ( key + " " + str(value) + ":" + str(dic[key]) + " / ")

#output and write
output = output[:-3]
print(output)
wfile.write(output)

#update shelves
print( "added new " + str( len(shdic) - bccnt ) + " words . ")
print( "file was saved as '" + write_file + "'")
bcdic.update(shdic)

shelf["index"] = bcdic
shelf["cnt"] = cnt

#close shelf
shelf.close()
wfile.close()
