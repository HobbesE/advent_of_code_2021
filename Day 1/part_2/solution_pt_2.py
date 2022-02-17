from os import lseek

data_list=[]

with open('data.txt') as file:
    for line in file.readlines():
        data_list.append(int(line))
        #create a list of values based on the data.txt file
    
#Solution for Part 1

increases_in_depth = 0
# #set increases_in_depth = 0 to count incremental increases in depth of ocean
# for i in range(len(data_list)-1):
# #for each value, if there is a value following it, compare the two
#     if data_list[i+1] > data_list[i]:
#         increases_in_depth += 1 
# #if the second value is greater than the first, i+1
# #break when there is not a value following the first value
# print(increases_in_depth)   

#Solution for Part 2

#set increases_in_depth = 0 to count incremental increases in depth of ocean
#for each value, if there are two values following it
for i in range(len(data_list)-3):
#group the focus data value with the following two data values and take the average
#assign the group's average to 'focus_average'
    focus_average = (data_list[i] + data_list[i+1] + data_list[i+2])
    comparative_average = (data_list[i+1] + data_list[i+2] + data_list[i+3])
    if focus_average < comparative_average:
        increases_in_depth += 1

#if the comparative_average value is greater than the focus_value, 
#break when there is not a value following the first value
print(increases_in_depth)   
