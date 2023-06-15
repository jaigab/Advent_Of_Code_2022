import os

filepath = input("What's the filepath for the data? ")

with open(filepath,"r") as data:
    result = data.read().split("\n")
    
class Regis:
    cycle=0
    vallog={}
    def __init__(self,value): self.val=value
    
    #Define a function in the class that inputs an instruction for the register and moves to the next cycle accordingly 
    
    def cpu(self,instruct):
        if instruct.split()[0]=="addx":
            self.val+=int(instruct.split()[1])
            Regis.cycle+=2
        if instruct[:4]=="noop": Regis.cycle+=1

#Create "X" in register class

X=Regis(1)

#Create a list to hold the values of X at cycles of multiples of 20

values20=[]
values={}

#Run through the instructions in the inputed results and apply to the cpu function of X

for i in range(len(result)):
    X.cpu(result[i])
    values[X.cycle]=X.val

#Add the values of X at cycles of multiples of 20 to the empty list and sum    
    
for m in range(20,240,40):
    for i in range(len(result)):
        if list(values)[i]>=int(m):
            values20+=[values[list(values)[i-1]]*m]
            break

print("The sum of the 6 signal strengths at 20th, 60th, 100th, 140th, 180th, and 220th cycles is " + str(sum(values20)))

#Define a class called Regis to log the value of register X while it completes each cycle, add a class item to log the value of previous cylces

class Regis:
    cycle=0
    vallog=[1,1]
    def __init__(self,value): self.val=value
    def cpu(self,instruct):
        if instruct.split()[0]=="addx":
            self.val+=int(instruct.split()[1])
            Regis.cycle+=2
            Regis.vallog+=[self.val]
            Regis.vallog+=[self.val]
        if instruct[:4]=="noop": 
            Regis.cycle+=1
            Regis.vallog+=[self.val]

#Create an empty list to display the CRT message            
            
crt=[]
for i in range(6):
    templ=[]
    for j in range(40): templ+=["."]
    crt+=[templ]

#Define the register X as class Regis and cycle through the instruction in the input data using the cpu function    
    
X=Regis(1)
for i in range(len(result)): X.cpu(result[i])

#Define a counter which checks the X value log at each cycle to see if any pixel in the "sprite" (3 pixels wide) is lit

counter=0
for j in range(6):
    for i in range(40):
        if X.vallog[(j*40)+i]==counter or X.vallog[(j*40)+i]==counter+1 or X.vallog[(j*40)+i]==counter-1: crt[j][i]="#"
        counter+=1
    counter=0

#Turn the list crt into a string for easier viewing    

crtstr=""
for i in crt:
    for j in i:
        crtstr=crtstr+str(j)
    crtstr=crtstr+"\n"
print("The 8 capital letters on the CRT are " + crtstr)