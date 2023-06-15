import os
data=input("What is the filepath for the data? ")
puzzle_input=[]
for line in open(data): puzzle_input = line

def search_string_in_groups_of_n(INPUT,N):
    for group in range(len(INPUT) - N):
        group_to_test = ""
        for character in range(N): group_to_test += INPUT[character + group]
        counter = 0
        for character in group_to_test:
            if group_to_test.count(character) >= 2: counter += 1
        if counter == 0:
            break
    return group
        
group_of_4_start_marker = search_string_in_groups_of_n(puzzle_input,4)
        
position_of_start_marker = group_of_4_start_marker + 4
print(str(position_of_start_marker) + " characters need to be processed before the first start-of-packet marker is reached when assesing in groups of 4")

group_of_14_start_marker = search_string_in_groups_of_n(puzzle_input,14)
        
position_of_start_marker = group_of_14_start_marker + 14
print(str(position_of_start_marker) + " characters need to be processed before the first start-of-packet marker is reached when assesing in groups of 14")
