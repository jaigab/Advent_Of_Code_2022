#Import and clean data

import os
data=input("What's the filepath for the input data?")
results=[]
for i in open(data): results+=[i.strip('\n')]

#Read commands and directories and add to a dictionary of file sizes

templist=[]
directory={}
for i in range(len(results)):
    if results[i][:4]=='$ cd' and results[i]!='$ cd ..': templist+=[results[i][5:]]
    if results[i]=='$ cd ..': templist.pop()
    if results[i][:4]=='$ ls':
        counter=[]
        items=[]
        directory[str(templist)]=[]
        for l in range(i,len(results)):
            if results[l][:4]=='dir ': counter+=[l]
            if results[l][:4]=='$ cd': break
            if results[l][0].isnumeric()==True: items+=[int(results[l].split()[0]),results[l].split()[1]]
            else: continue
        for m in counter: directory[str(templist)].append(results[m][4:])
        directory[str(templist)].append(items)

#Calculate file size of the items in each directory        

filesize={}
for item in directory:
    if item==[]:continue
    else: 
        templist=[]
        for j in directory[item][-1]:
            if type(j)==int: templist+=[j]
    filesize[item]=sum(templist)

#Calculate filesize of directory including sub-directories and add directories under 100000 to dictionary
    
filesize2={}
filesize_100000={}
for item in filesize.keys():
    templist=[]
    counter=0
    for j in filesize.keys():
        if item[:-1]==j[:len(item)-1]:
            counter+=1
            templist+=[filesize[j]]
    filesize2[item]=sum(templist)
    if sum(templist)<100000: filesize_100000[item]=sum(templist)

#Sum directories under 100000
        
templist=[]
for item in filesize_100000:
    templist+=[filesize_100000[item]]
print("The solution to part 1 is: " +str(sum(templist)))

#Find smallest directory to free up space

for item in reversed(sorted(filesize2.items(), key=lambda x:x[1])):
    if item[1]<=8381165:
        print("The solution to part 2 is: " + item)
        break
