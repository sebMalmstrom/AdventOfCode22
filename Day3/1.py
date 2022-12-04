path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

priorityString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

sumOfPrio = 0

for x in my_list:
    string1 = x[:len(x)//2]
    string2 = x[len(x)//2:]
    matching = set(string1) & set(string2)
    sumOfPrio += priorityString.find(matching.pop()) + 1
print(sumOfPrio)