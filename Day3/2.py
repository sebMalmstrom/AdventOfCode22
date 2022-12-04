path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

priorityString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sumOfPrio = 0

for i in range(0, len(my_list), 3):
    set1 = set(my_list[i])
    set2 = set(my_list[i+1])
    set3 = set(my_list[i+2])
    matching = set1 & set2 & set3
    sumOfPrio += priorityString.find(matching.pop()) + 1
print(sumOfPrio)