import os
data=input("What's the filepath for the data?")
puzzle_input=[]
for line in open(data):puzzle_input+=[line]

def clean_puzzle_input(INPUT):
    OUTPUT=[]
    for line in INPUT[:9]:
        item_list=[]
        for item in line: item_list.append(item)
        OUTPUT+=[item_list]
        
    crate_dictionary={}
    index = 0
    for stack in range(1,34,4):
        crate_info=[]
        for crate in reversed(range(0,8)): crate_info += [OUTPUT[crate][stack]]
        index += 1
        crate_dictionary[index] = crate_info
        
    clean_crate_dictionary={}
    for crate in range(1,len(crate_dictionary)+1):
        crate_info=[]
        for stack in range(len(crate_dictionary[crate])):
            if crate_dictionary[crate][stack]!=' ': crate_info += crate_dictionary[crate][stack]
        clean_crate_dictionary[crate]=crate_info
        
    clean_instructions=[]
    for instruction in puzzle_input[10:]: clean_instructions+=[[int(instruction.split()[1]),int(instruction.split()[3]),int(instruction.split()[5])]]
    
    return clean_crate_dictionary,clean_instructions

cleaned_input , cleaned_instruction = clean_puzzle_input(puzzle_input)

class StackOfCrates:
    def __init__(self, dictionary):
        self.stacks = dictionary
        
    def move_crates_part1(self,instruction):
        for move in range(instruction[0]):
            self.stacks[instruction[2]].append(self.stacks[instruction[1]][-1])
            self.stacks[instruction[1]].pop() 
    
    def move_crates_part2(self,instruction):
        templ=[]
        for i in range(instruction[0]):
            templ=templ+[self.stacks[instruction[1]][-1]]
            self.stacks[instruction[1]].pop()
        for j in reversed(range(len(templ))): self.stacks[instruction[2]].append(templ[j])        
        
crate_stacks = StackOfCrates(cleaned_input)            

for instruction in cleaned_instruction: crate_stacks.move_crates_part1(instruction)  
    
last_crate=""
for stack in range(1,10): last_crate += crate_stacks.stacks[stack][-1]
print("The crates that end up at the top of each stack are " + str(last_crate))

cleaned_input , cleaned_instruction = clean_puzzle_input(puzzle_input)

crate_stacks = StackOfCrates(cleaned_input) 

for instruction in cleaned_instruction: crate_stacks.move_crates_part2(instruction)
last_crate=""
for stack in range(1,10): last_crate += crate_stacks.stacks[stack][-1]
print("The crates that end up at the top of each stack are " + str(last_crate))