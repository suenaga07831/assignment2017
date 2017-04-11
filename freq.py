"""
Task2.3 (9)
open file(cv000_***) from input
and output frequency

"""

#import inputdata
import sys
args = sys.argv

#define filename/filemode
if len(args) == 2 :
    fn = args[1]
    fm = "r"

else :
    print("please write by this format")
    print("grep.py <import file>")
    quit()
    
#open file
f = open(fn,fm)

#combine in 1 line
disp =""
dict = {}
for i in f:
    disp += i

#list up
disp = disp.split(" ")

#register dict
cnt = 0
for i in disp:
    i = i.strip("\n")
    disp[cnt] = i
    cnt += 1

    dict[i] = 0
    
#count
for word in disp:
    for key in dict.iterkeys():
        if key == word:
            dict[key] += 1
            break

#sort and output
for key,value in sorted(dict.items() , key = lambda x:x[1],reverse = True):
    print value , key

#close file
f.close()
