#Import data

import os
data=input("What is the filepath for the input data?")
results=[]
for i in open(data): results+=[i.strip('\n')]

#Define function tat checks if tree is visible by dictionary of tree heights in each direction

def isvis(grid,tree):
    templist=[False]
    direction=["up","down","left","right"]
    for coord in direction:
        if grid[coord]==[]: return True
    else:
        for item1 in direct:
            for tree_neighbour in grid[item1]:
                if tree_neighbour>=tree:
                    templist.append(False)
                    break
        if len(templist)>=5: return False
        else: return True

#Read the grid of trees to produce a dictionary of trees for each item going in each direction

gridbool=[]
directions={}
direct=["up","down","left","right"]
for line in range(len(results)):
    templist=[]
    for item in range(len(results[line])):
        for coord in direct: directions[coord]=[]
        for i in range(0,line): directions["up"]+=[int(results[i][item])]
        for i in range(line+1,len(results)): directions["down"]+=[int(results[i][item])]
        for i in range(0,item): directions["left"]+=[int(results[line][i])]
        for i in range(item+1,len(results[line])): directions["right"]+=[int(results[line][i])]
        templist=templist+[isvis(directions,int(results[line][item]))]
    gridbool=gridbool+[templist]

#Count the number of visible trees  

counter=0   
for line in gridbool:
    for item in line:
        if item==True: counter+=1
        else: continue
print("The solution to part 1 is: "+str(counter))

#Define function to find scenice visibility list for each tree

def visbility(grid,tree):
    templist=[]
    direct=["up","down","left","right"]
    for coord in direct:
        counter=0
        for item in range(len(grid[coord])):  
            if grid[coord][item]<tree: counter+=1
            else: break
        if len(grid[coord])!= counter: counter+=1
        templist+=[counter]
    return templist

#Define function to multiply all values in list

def multiply(list1):
    prod=1
    for i in list1: prod=prod*i
    return prod

#Read the grid of trees to produce a dictionary of trees for each item going in each direction which "up" and "left" lists reveresed to preserve tree order

visgrid=[]
directions={}
direct=["up","down","left","right"]
for line in range(len(results)):
    templist=[]
    for item in range(len(results[line])):
        for coord in direct: directions[coord]=[]
        for i in reversed(range(0,line)): directions["up"]+=[int(results[i][item])]
        for i in range(line+1,len(results)): directions["down"]+=[int(results[i][item])]
        for i in reversed(range(0,item)): directions["left"]+=[int(results[line][i])]
        for i in range(item+1,len(results[line])): directions["right"]+=[int(results[line][i])]
        templist+=[multiply(visbility(directions,int(results[line][item])))]
    visgrid+=[templist]

#Find tree with highest scenic factor

listvis=[]
for line in visgrid:
    for item in line: listvis+=[item]
print("The solution to part 2: " + str(sorted(listvis)[-1]))