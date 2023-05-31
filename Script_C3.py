#Import and clean data

import os
import string
data=input("What's the filepath for the data? ")
puzzle_input=[]
for i in open(data):puzzle_input+=[i.strip("\n")]

def item_not_matching(STRING1,STRING2):
    for item in STRING1:
        if STRING2.find(item) != -1: not_matched_list = [item]
    return not_matched_list   
    
alphabet_to_number_map={}
for number in range(1,27):
    alphabet_to_number_map[list(string.ascii_lowercase)[number-1]]=number
    alphabet_to_number_map[list(string.ascii_uppercase)[number-1]]=number+26
    
rucksacks=[]

for rucksack in puzzle_input: rucksacks += [[rucksack[:(int(len(rucksack)/2))],rucksack[(int(len(rucksack)/2)):]]]

not_matched_list = []
for rucksack in rucksacks: not_matched_list += item_not_matching(rucksack[0],rucksack[1])
item_prioritization_mapping = []
for item in not_matched_list: item_prioritization_mapping += [alphabet_to_number_map[item]]
print("The sum of the priorities of the items that appear in both compartments of each rucksack is " + str(sum(item_prioritization_mapping)))

def items_matching_in_3_group(STRING1,STRING2,STRING3):
    matched_string_1_2 = []
    matched_string_1_2_3 = []
    for item in STRING1: 
        if STRING2.find(item) != -1: matched_string_1_2 += [item]
    for item in matched_string_1_2:
        if STRING3.find(item) != -1: matched_string_1_2_3 = [item]
    return matched_string_1_2_3

three_rucksacks_groups = []
for index in range(0,len(puzzle_input),3): three_rucksacks_groups += [[puzzle_input[index],puzzle_input[index + 1],puzzle_input[index + 2]]]

badge_list = []
for three_elf_group in three_rucksacks_groups: badge_list += items_matching_in_3_group(three_elf_group[0],three_elf_group[1],three_elf_group[2])
item_prioritization_mapping = []
for badge in badge_list: item_prioritization_mapping += [alphabet_to_number_map[badge]]
print("The sum of the priorities of each three-elf group is " + str(sum(item_prioritization_mapping)))