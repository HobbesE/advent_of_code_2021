from os import lseek


data_list=[]

with open('data.txt') as file:
    for line in file.readlines():
        data_list.append(int(line))
        #create a list of values based on the data.txt file
    
increases_in_depth = 0
#set increases_in_depth = 0 to count incremental increases in depth of ocean
for i in range(len(data_list)-1):
#for each value, if there is a value following it, compare the two
    if data_list[i+1] > data_list[i]:
        increases_in_depth += 1 
#if the second value is greater than the first, i+1
#break when there is not a value following the first value
print(increases_in_depth)   