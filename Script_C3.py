#Import and clean data

import os
import string
data=input("What's the filepath for the data")
results=[]
for i in open(data):results+=[i.strip("\n")]

#Define letter mapping to priority number

alph_map={}
for i in range(1,27):
    alph_map[list(string.ascii_lowercase)[i-1]]=i
    alph_map[list(string.ascii_uppercase)[i-1]]=i+26
compart_results=[]

#Split strings into items in each compartment

for i in results: compart_results+=[[i[:(int(len(i)/2))],i[(int(len(i)/2)):]]]
    
#Define function to find not matching letter in 2 strings
    
def letter_notmatch(string1,string2):
    for i in string1:
        if string2.find(i) != -1: unmatched=[i]
    return unmatched

#Apply fucntion to all items in data and map items to numbers then sum

nmatch_list=[]
for i in compart_results: nmatch_list+=letter_notmatch(i[0],i[1])
prio_match=[]
for i in nmatch_list:prio_match+=[alph_map[i]]
print("Solution to part 1 is: "+str(sum(prio_match)))

#Clean data and group into 3s

part2_results=[]
for i in range(0,len(results1),3): part2_results+=[[results1[i],results1[i+1],results1[i+2]]]
    
#Define function to find matching letters in 3 strings

def letter_match(string1,string2,string3):
    matched1=[]
    matched2=[]
    for i in string1: 
        if string2.find(i) != -1: matched1+=[i]
    for j in matched1:
        if string3.find(j) != -1: matched2=[j]
    return matched2

#Apply function to all items in data and map to numbers then sum

nmatch_list=[]
for i in part2_results: nmatch_list+=letter_match(i[0],i[1],i[2])
prio_match=[]
for i in nmatch_list: prio_match+=[alph_map[i]]
print("Solution to part 2 is: " +str(sum(prio_match)))