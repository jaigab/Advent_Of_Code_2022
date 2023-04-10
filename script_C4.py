#Import data

import os
data=input("What's the filepath for the data?")
clean_data=[]
for i in open(data): 
    tempv=i.strip('\n').split(',')[0].split("-"),i.strip('\n').split(',')[1].split("-")
    templist=[]
    for j in tempv:
        templist+=[[int(j[0]),int(j[1])]]
    clean_data+=[templist]
    
#Define function to check if one set of numbers inside range of another

def insidecheck(list1,list2):
    if list2[1]>=list1[1] and list2[0]<=list1[0]:
        return True
    if list1[1]>=list2[1] and list1[0]<=list2[0]:
        return True
    else:
        return False

#Apply function to dataset and count
    
boolcheck=[]
counter=0
for i in clean_data:
    boolcheck+=[insidecheck(i[0],i[1])]
    if insidecheck(i[0],i[1])==True:
        counter+=1
print("The solution to part 1 is: " + str(counter))

#Define function that checks if there is any overlap in ranges

def overlapcheck(list1,list2):
    for i in range(list1[0],list1[1]+1,1):
        for j in range(list2[0],list2[1]+1,1):
            if i==j:
                return True
                break

#Apply function to dataset and count                
                
counter=0
for i in clean_data:
    if overlapcheck(i[0],i[1]) == True:
        counter+=1
print("The solution to part 2: " + str(counter))