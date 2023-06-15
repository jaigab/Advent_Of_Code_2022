import os
data=input("What is the filepath for the data? ")
puzzle_input=[]
for line in open(data): puzzle_input+=[line.strip('\n')]

filepath=[]
directory={}
for command in range(len(puzzle_input)):
    if puzzle_input[command][:4] == '$ cd' and puzzle_input[command] != '$ cd ..': filepath += [puzzle_input[command][5:]]
    elif puzzle_input[command] == '$ cd ..': filepath.pop()
    elif puzzle_input[command][:4] == '$ ls':
        index = []
        file_sizes = []
        directory[str(filepath)] = []
        for sub_files in range(command,len(puzzle_input)):
            if puzzle_input[sub_files][:4] == 'dir ': index += [sub_files]
            elif puzzle_input[sub_files][:4] == '$ cd': break
            elif puzzle_input[sub_files][0].isnumeric() == True: file_sizes += [int(puzzle_input[sub_files].split()[0]),puzzle_input[sub_files].split()[1]]
            else: continue
        for number in index: directory[str(filepath)].append(puzzle_input[number])
        directory[str(filepath)].append(file_sizes)

directory_with_filesize = {}
for filepath in directory:
    if filepath == []:continue
    else: 
        file_size_list = []
        for file in directory[filepath][-1]:
            if type(file) == int: file_size_list += [file]
    directory_with_filesize[filepath] = sum(file_size_list)
    
directory_with_sub_directory_filesize = {}
directories_under_100000 = {}
for filepath in directory_with_filesize.keys():
    sub_directory_files_size = []
    counter = 0
    for sub_filepath in directory_with_filesize.keys():
        if filepath[:-1] == sub_filepath[:len(filepath)-1]:
            counter += 1
            sub_directory_files_size += [directory_with_filesize[sub_filepath]]
    directory_with_sub_directory_filesize[filepath] = sum(sub_directory_files_size)
    if sum(sub_directory_files_size) < 100000: directories_under_100000[filepath] = sum(sub_directory_files_size)
        
total_file_sizes_under_100000 = []
for filepath in directories_under_100000:
    total_file_sizes_under_100000+=[directories_under_100000[filepath]]
print("The total sum of the directories under filesize = 100000 is " + str(sum(total_file_sizes_under_100000)))

unused_space_required = input("How much unused space is required for the update?")

for filepath in reversed(sorted(directory_with_sub_directory_filesize.items(), key=lambda x:x[1])):
    if filepath[1]<=unused_space_required:
        print("The filepath and size for the smallest directory that can be deleted to free up enough space is " + str(filepath))
        break