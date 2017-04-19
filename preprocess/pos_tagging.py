"""
Task2.4(3)
open file from input
and tagging by senna tagger
"""

#define var
cnt = 0           #counter
flist = []        #file list
linked_file = ""  #linked file
ifile = ""        #input file data
splited_file = [] #splited file
taged_file = []   #taged file
f = ""            #filename


import os.path
import nltk

#import Senna Tagger
from nltk.tag import SennaTagger
tagger = SennaTagger('/usr/share/senna-v3.0')

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
splited_file = nltk.sent_tokenize(linked_file)

#tagging 1 sentence
[print(x) for x in tagger.tag(splited_file[0].split())]


"""
#tagging all sentence

#tagging and output
for i in splited_file:
    [print(x) for x in tagger.tag(i.split())]
"""

