"""
Task2.3 (9)
open file(cv000_***) from input
and output frequency

"""

#import inputdata
import sys
args = sys.argv

#define filename/filemode
if len(args) == 1 :
    fn = input("please filename: ")
    fm = "r"
        
else :
    print("please write by this format")
    print("freq.py")
    quit()
    
#open file
f = open(fn,fm)

#combine in 1 line
disp=""
dic = {}

for i in f:
    disp += i
    disp = disp.rstrip("\n")

#list up
disp = disp.split(" ")

#register dic
for i in disp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
#sort and output
for key , value in sorted(dic.items() , key = lambda x:x[1] ):
    print(str(value) + key)



#close file
f.close()
