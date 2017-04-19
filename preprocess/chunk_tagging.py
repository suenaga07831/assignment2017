"""
Task2.4(4)
open file from input
and chunk tagging by senna tagger
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

#import senna chk taggar
from nltk.tag import SennaChunkTagger
chktagger = SennaChunkTagger('/usr/share/senna-v3.0')

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

#chunk tagging first sentence
[print(x) for x in chktagger.tag(splited_file[0].split())]

"""
#chunk taggin all sentences

#tagging and output
for i in splited_file:
    [print(x) for x in chktagger.tag(i.split())]
"""
