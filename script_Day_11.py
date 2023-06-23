import os
filepath=input("What's the filepath for the data? ")
with open(filepath,"r") as data:
    realdata=[]
    for i in data: realdata += [i.split("\n")[0]]

#Define class of "Monkey" that includes all the properties that each monkey has

class Monkey:
    def __init__(self,data):
        itemlist=[]
        for n in data[1].split(" "):
            if n.strip(",").isdigit()==True: itemlist+=[int(n.strip(","))]
        self.item=itemlist
        self.op=data[2].split("=")[1].split(" ")[1:]
        self.test=int(data[3].split()[-1])
        self.TRUE=int(data[4].split()[-1])
        self.FALSE=int(data[5].split()[-1])
        self.inspectcount=0

#Define a method that runs through the list of items for each monkey, applys the operation and test and moves the item to the appropriate monkey for part 1        

#For part 2, the value of the item is mod by a "modfactor" to keep it from becoming too large now
#This modfactor is the product of all the test factors for all monkeys. 
#This works as we only need to know if the number is divisible by the test and we know that all multiples of this "modfactor"
#will be divisible in all tests. The mod of the number after this modfactor will determine whether the item number is divisible or not.

    def operation(self,data,part):
        for item in self.item[:]:
            if part==1:
                if self.op[2]=="old": val=int((item**2)/3//1)
                elif self.op[1]=="*" and self.op[2]!="old": val=int((item*int(self.op[2]))/3//1)
                elif self.op[1]=="+": val=int((item+int(self.op[2]))/3//1)
                if val%self.test==0: data[self.TRUE].item+=[val]
                elif val%self.test!=0: data[self.FALSE].item+=[val]
                self.item.remove(item)
                self.inspectcount+=1
            elif part==2:
                if self.op[2]=="old": val=int((item**2)//1)
                elif self.op[1]=="*" and self.op[2]!="old": val=int((item*int(self.op[2]))//1)
                elif self.op[1]=="+": val=int((item+int(self.op[2]))//1)
                if val%self.test==0: data[self.TRUE].item+=[val%modfactor]
                elif val%self.test!=0: data[self.FALSE].item+=[val%modfactor]
                self.item.remove(item)
                self.inspectcount+=1 

monkeys={}
for item in range(8):
    monkeys[item]=Monkey(realdata[item*7:(item*7)+6])
    
for iteration in range(20):
    for item in range(8): monkeys[item].operation(monkeys,1) 
countlist=[]    
for item in range(8): countlist+=[monkeys[item].inspectcount]
print("The level of monkey business after 20 rounds is " + str(sorted(countlist,reverse=True)[0]*sorted(countlist,reverse=True)[1]))

monkeys2={}
modfactor=1
for item in range(8):
    monkeys2[item]=Monkey(realdata[item*7:(item*7)+6])
    modfactor=modfactor*monkeys2[item].test
    
for iteration in range(10000):
    for item in range(8): monkeys2[item].operation(monkeys2,2) 
countlist=[]    
for item in range(8): countlist+=[monkeys2[item].inspectcount]
print("The level of monkey business after 10,000 rounds is " + str(sorted(countlist,reverse=True)[0]*sorted(countlist,reverse=True)[1]))
