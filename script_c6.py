#Import data

import os
data=input("What is the filepath for the data?")
results=[]
for i in open(data): results=i

#Search through data in groups of 4 to see strings with unmatched character
    
for j in range(len(results)-4):
    templist=""
    for l in range(4):templist+=results[l+j]
    counter=0
    for n in templist:
        if templist.count(n)>=2: counter+=1
    if counter==0:
        break
print("The solution to part 1 is: " + str(j+4))

#Search through data in groups of 14 to see strings with unmatched character

for j in range(len(results)-14):
    tempstr=""
    for l in range(14): tempstr+=results[l+j]
    counter=0
    for n in tempstr:
        if tempstr.count(n)>=2: counter+=1
    if counter==0:
        break

print("The solution to part 2 is: " + str(j+14))