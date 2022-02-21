
data_list =[]

with open('data.txt') as f:
    for line in f.readlines():
        data = line.split()
        data_list.append([data[0],int(data[1])])
        # that gets me a list of list values like ['up', 1]

x=0
y=0

for value in data_list:
    if value[0] == 'forward':
        x += value[1]
    if value[0] == 'up':
        y -= value[1]
    if value[0] == 'down':
        y += value[1]

print(f'The end coordinates are {x},{y}')
print(f'The Advent of Code solution is {x*y}')

# goal: {x : 315, y: -14}

