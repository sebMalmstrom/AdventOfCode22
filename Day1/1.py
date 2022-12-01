path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

highest = 0
nextTry = []
for line in my_list:
    if line == '':
        highest = max(highest, sum(nextTry))
        nextTry = []
        continue
    print(line)
    nextTry.append(int(line))
print(highest)