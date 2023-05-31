import os

data=input("What's the filepath for the data? ")
puzzle_input=[]
for item in data: puzzle_input+=item.split("\n")

def clean_input(PUZZLE_INPUT):  
    cleaned_puzzle_input = {}
    elf_index = 0
    elf_item_list = []
    for item in PUZZLE_INPUT:
        if item != '': elf_item_list += [int(item)]
        else: 
            cleaned_puzzle_input[elf_index] = elf_item_list
            elf_item_list = []
            elf_index += 1
    return cleaned_puzzle_input

all_elf_item_list = clean_input(puzzle_input)
        
total_calories_per_elf={}
for elf in range(len(all_elf_item_list)):
    total_calories_per_elf[elf] = sum(all_elf_item_list[elf])
    
sorted_calorie_intakes = sorted(total_calories_per_elf.items(), key=lambda x:x[1], reverse=True)
highest_calorie_intakes = sorted_calorie_intakes[0]
print("Elf #" + str(highest_calorie_intakes[0]) + " Has the highest calorie intake of " +str(highest_calorie_intakes[1]))

top_3_calorie_intake_sum = 0
for item in range(3):
    top_3_calorie_intake_sum += sorted_calorie_intakes[item][1]
print("The top 3 elves have a combined calorie intake of " + str(top_3_calorie_intake_sum))
