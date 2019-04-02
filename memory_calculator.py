

import os

# Write a program that list the files in the current directory and the percentage of total memory used
# First step: Get the total memory size of the directory

def calculate_total_size_directory(current_path):
    total_memory_usage = 0
    for entry_file in os.sandir(current_path):
        file_memory_size = entry_file.stat(follow_symlinks=False).st_size
        total_memory_usage +=file_memory_size
    return total_memory_usage

total_directory_memory_usage = calculate_total_size_directory('.')

file_list = []
file_memory_percentage_list = []

for entry_file in os.scandir('.'):
    filename = entry_file.name
    percentage_memory_filename = int(entry_file.stat(follow_symlinks=False).st_size/total_directory_memory_usage*100)
    file_list.append(filename)
    file_memory_percentage_list.append(percentage_memory_filename)

for index in range(len(file_list)):
    print(file_list[index] + " - " + str(file_memory_percentage_list[index])+"%")

# DONE!!!!!!