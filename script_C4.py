import os
data=input("What's the filepath for the data")
puzzle_input = []
for line in data: puzzle_input += [[line.split("\n")[0].strip('\n').split(',')[0].split("-"),line.strip('\n').split(',')[1].split("-")]]
    
def check_numbers_in_range(NUMBERS,NUMBER_RANGE):
    if int(NUMBER_RANGE[1]) >= int(NUMBERS[1]) and int(NUMBER_RANGE[0]) <= int(NUMBERS[0]):
        return True
    elif int(NUMBERS[1]) >= int(NUMBER_RANGE[1]) and int(NUMBERS[0]) <= int(NUMBER_RANGE[0]):
        return True
    else:
        return False
    
assignment_pairs_containment_list = []
index = 0
for assignment_pairs in puzzle_input:
    assignment_pairs_containment_list += [check_numbers_in_range(assignment_pairs[0],assignment_pairs[1])]
    if check_numbers_in_range(assignment_pairs[0],assignment_pairs[1]) == True:
        index += 1
print("There are " +str(index) + " assignment pairs where one range fully contains the other")

def check_overlap_between_ranges(RANGE1,RANGE2):
    for number in range(int(RANGE1[0]),int(RANGE1[1])+1,1):
        for number2 in range(int(RANGE2[0]),int(RANGE2[1])+1,1):
            if number == number2:
                return True
                break                
                
index = 0
for assignment_pairs in puzzle_input:
    if check_overlap_between_ranges(assignment_pairs[0],assignment_pairs[1]) == True:
        index += 1
        
print("There are " +str(index) + " assignment pairs where one range overlaps the other")