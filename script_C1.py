import os

#Import data from txt file

data=input("What's the filepath for the data?")
results =[]
for i in open(data): results+=[i]

#Clean data and turn into int

results1={}
elfcount=0
tempcal=[]
for i in results:
    if i !='\n': tempcal+=[int(i[:-1])]
    else:
        results1[elfcount]=tempcal
        tempcal=[]
        elfcount+=1

#Calculate total calorie intake for each elf

totalcal={}
elfcount=0
for i in results1:
    totalcal[elfcount]=sum(results1[elfcount])
    elfcount+=1

#Sort calorie intakes to find highest

print("Solution to part 1 is: " + str(sorted(totalcal.items(), key=lambda x:x[1], reverse=True)[0:3]))

sortedtotalcal=sorted(totalcal.items(), key=lambda x:x[1], reverse=True)
topthreecal=0
for item in range(3):
    topthreecal+=sortedtotalcal[item][1]
print("Solution to part 2 is: " +str(topthreecal))
