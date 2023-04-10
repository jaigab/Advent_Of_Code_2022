#Import data

import os
data=input("What's the filepath for the data?")
results=[]
for i in open(data):results+=[i]

#Clean crates data

crates=[]
for i in results[:9]:
    templ=[]
    for j in i: templ.append(j)
    crates+=[templ]

#Turn crate data into a dictionary and transpose

cratedict={}
counter=0
for i in range(1,34,4):
    templist=[]
    for j in reversed(range(0,8)): templist+=[crates[j][i]]
    counter+=1
    cratedict[counter]=templist
clean_cratedict={}
for j in range(1,len(cratedict)+1):
    templist=[]
    for i in range(len(cratedict[j])):
        if cratedict[j][i]!=' ': templist+=[cratedict[j][i]]
    clean_cratedict[j]=templist

#Clean move instruction data

cleaned_instr=[]
for i in results[10:]: cleaned_instr+=[[int(i.split()[1]),int(i.split()[3]),int(i.split()[5])]]

#Define function that applies the move instructions to the crate dictionary

def cratemove(cratediction,move):
    for i in range(move[0]):
        cratediction[move[2]].append(cratediction[move[1]][-1])
        cratediction[move[1]].pop()
    return cratediction    
    
#Apply function to data and create string of top crates in each piles

for i in cleaned_instr: cratemove(clean_cratedict,i)

lastcrate=""
for i in range(1,10): lastcrate+=clean_cratedict[i][-1]
print("The solution to part 1 is :" + str(lastcrate))

#Turn crate data into a dictionary and transpose

clean_cratedict={}
for j in range(1,len(cratedict)+1):
    templist=[]
    for i in range(len(cratedict[j])):
        if cratedict[j][i]!=' ': templist+=[cratedict[j][i]]
    clean_cratedict[j]=templist
    
#Define new function    
    
def cratemove9001(cratedict,move):
    templ=[]
    for i in range(move[0]):
        templ=templ+[cratedict[move[1]][-1]]
        cratedict[move[1]].pop()
    for j in reversed(range(len(templ))): cratedict[move[2]].append(templ[j])
    return cratedict

#Apply function to data and create string of top crates in each piles

for l in cleaned_instr: cratemove9001(clean_cratedict,l)
lastcrate=""
for i in range(1,10): lastcrate+=clean_cratedict[i][-1]
print("The solution to part 2 is : " +str(lastcrate))