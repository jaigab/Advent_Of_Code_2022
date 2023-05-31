#Import data and clean data

data=input("What is the filepath for the input data? ")
results=[]
for i in open(data): results+=[i.strip('\n')]
moves=[]
for i in results: moves+=[[i.split()[0],int(i.split()[1])]]
           
#Define class for Head of rope that has method that operates on the position with a function "movement"

class Head:
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord
    def movement(self,direction):
        if direction=='R': self.x+=1
        if direction=='L': self.x-=1
        if direction=='U': self.y-=1
        if direction=='D': self.y+=1
        return self.x,self.y

#Define function to find the absolute value of a number
    
def Modulus(number):
    if number>=0:
        return number
    else:
        return int(number*(-1))

#Define class for Tail of rope that operates on the posiiton with a function called movement taking the position of the head as an argument     
    
class Tail:
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord
        
    #Using the modulus function, the movement direction of the tail can be dictated by its proximity to the head
    
    def movement(self,head):
        rope_x=head.x-self.x
        rope_y=head.y-self.y
        if Modulus(rope_x)==2: 
            self.x=self.x+int(rope_x/2)
            if Modulus(rope_y)==1:self.y=self.y+rope_y
            if Modulus(rope_y)==2:self.y=self.y+int(rope_y/3)
        if Modulus(rope_y)==2: 
            self.y=self.y+int(rope_y/2)
            if Modulus(rope_x)==1:self.x=self.x+rope_x
            if Modulus(rope_x)==2:self.x=self.x+int(rope_x/3)
        return self.x,self.y

#Create dictionary holding the estimated widths of the grid based on the highest deviation from origin due to moves being fulfilled

widthest={}
for i in ["RL","UD"]:
    widthest[i]=[1]
for i in moves:
    if i[0]=="R": widthest["RL"]+=[widthest["RL"][-1]+i[1]]
    if i[0]=="L": widthest["RL"]+=[widthest["RL"][-1]-i[1]]
    if i[0]=="U": widthest["UD"]+=[widthest["UD"][-1]-i[1]]
    if i[0]=="D": widthest["UD"]+=[widthest["UD"][-1]+i[1]]    
    
#Define a field and place the Head and Tail at the origin

field=[]
for line in range(max(widthest["UD"])-min(widthest["UD"])+20):
    templist=[]
    for item in range(max(widthest["RL"])-min(widthest["RL"])+20): templist=templist+['.']
    field=field+[templist]
H=Head(Modulus(min(widthest["RL"])),Modulus(min(widthest["UD"])))
T=Tail(Modulus(min(widthest["RL"])),Modulus(min(widthest["UD"])))

#Read through instructions and apply the movement functions to the head and tail objects

for line in moves:
    for num_moves in range(line[1]):
        H.movement(line[0])
        T.movement(H)
        field[T.y][T.x]='#'

#Create a new field so lines can be output as string if required and count the number of places the Tail reached        
        
strfield=[]
counter=0
for line in field:
    strfield=strfield+["".join(line)]
    for item in line:
        if item != '.': counter+=1
print("The solution to part 1 is: "+str(counter))

#Define a field of specific width and place the Head and Tail at the center

field=[]
for line in range(max(widthest["RL"])-min(widthest["RL"])+20):
    templist=[]
    for item in range(max(widthest["UD"])-min(widthest["UD"])+20): templist=templist+['.']
    field=field+[templist]
yco=Modulus(min(widthest["UD"]))+10
xco=Modulus(min(widthest["RL"]))+10
H=Head(xco,yco)
T=Tail(xco,yco)

#Define a dictionary "rope" that at any point has the coordinates of the point on the rope from 0(Head) to 9(Tail)

rope={}
count=[]
for item in range(1,10): rope[item]=Tail(xco,yco)

#Read through instructions and apply the movement functions to all points on the rope

for line in moves:
    for n in range(line[1]):
        H.movement(line[0])
        rope[0]=H
        for item in range(1,10):
            rope[item].movement(rope[item-1])
        field[rope[9].x][rope[9].y]="#"

#Create a new field so lines can be output as string if required and count the number of places the Tail reached        

strfield=[]
counter=0
for line in field:
    strfield=strfield+["".join(line)]
    for item in line:
        if item != '.': counter+=1
print("The solution to part 2 is: "+str(counter))