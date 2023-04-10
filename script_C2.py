#Import and clean data

import os
data=input("What is the filepath for the data?")
results=[]
for i in open(data): results+=[[i[0],i[2]]]

#Define rules of Rock, Paper, Scissors 
    
itemscore={'X':[1,3,0,6],'Y':[2,6,3,0],'Z':[3,0,6,3]}

#Apply rules to dataset

total=[]
counter=0
for i in results:
    total+=[[itemscore[i[1]][0]]]
    if i[0]=='A': total[counter]+=[itemscore[i[1]][1]]
    if i[0]=='B': total[counter]+=[itemscore[i[1]][2]] 
    if i[0]=='C': total[counter]+=[itemscore[i[1]][3]] 
    counter+=1

#Total point score for all rounds
    
total1=[]
for i in total: total1+=[sum(i)]
print("Solution to part 1 is: " +str(sum(total1)))

#Define new rules of Rock, Paper, Scissors 

fixed_itemscore={'X':[0,3,1,2],'Y':[3,1,2,3],'Z':[6,2,3,1]}

#Apply new rules to dataset

fixed_strategy=[]
counter=0
for i in results: 
    fixed_strategy+=[[fixed_itemscore[i[1]][0]]]
    if i[0]=='A': fixed_strategy[counter]+=[fixed_itemscore[i[1]][1]]
    if i[0]=='B': fixed_strategy[counter]+=[fixed_itemscore[i[1]][2]]
    if i[0]=='C': fixed_strategy[counter]+=[fixed_itemscore[i[1]][3]]
    counter+=1

#Total point score for all rounds with new strategy
    
fixed_strategy_total=[]
for i in fixed_strategy: fixed_strategy_total+=[sum(i)]
print("Solution to part 2 is: " +str(sum(fixed_strategy_total)))