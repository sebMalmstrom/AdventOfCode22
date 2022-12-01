path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

listOfEntries = []
nextTry = []
for line in my_list:
    if line == '':
        listOfEntries.append(sum(nextTry))
        nextTry = []
        continue
    nextTry.append(int(line))

listOfEntries.sort()
listOfEntries.reverse()
print(listOfEntries)

print(sum(listOfEntries[:3]))

