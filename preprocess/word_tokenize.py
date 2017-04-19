"""
Task2.4(2)
open file from input
and split word  by NLTK
"""

#define var
cnt = 0      #counter
flist = []   #file list
lfile = ""   #linked file
sfile = []   #file splited by sentence
wfile = []   #file splited by word
ifile = ""   #input file data
f = ""       #filename
s = ""       #sentence
w = ""       #word

import os.path
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

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
    lfile += f.read()
    
    #close file
    f.close

#split file
sfile = sent_tokenize(lfile)

for sentence in sfile:
    w = word_tokenize(sentence)

    for word in w:
        wfile.append(word)


print(wfile)
