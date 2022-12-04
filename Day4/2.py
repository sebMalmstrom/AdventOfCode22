
path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

count = 0

for x in my_list:
    splitX = x.split(',')
    string1 = splitX[0].split('-')
    string2 = splitX[1].split('-')
    set1 = set(range(int(string1[0]), int(string1[1]) +1))
    set2 = set(range(int(string2[0]), int(string2[1]) +1))
    
    if len(set1 & set2) > 0:
        count += 1
print(count)