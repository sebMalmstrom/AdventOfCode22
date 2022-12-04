path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

totaltPoint = 0

for x in my_list:
    splitX = x.split(' ')
    if len(splitX) == 2:

        if splitX[1] == 'Y': # Paper
            totaltPoint += 2
            if splitX[0] == 'A': # Rock
                totaltPoint += 6
            elif splitX[0] == 'B': # Paper
                totaltPoint += 3
            else: # Scissor
                totaltPoint += 0
        
        elif splitX[1] == 'Z': # Scissor
            totaltPoint += 3
            if splitX[0] == 'A': #Rock
                totaltPoint += 0
            elif splitX[0] == 'B': #Paper
                totaltPoint += 6
            else: #Scissor
                totaltPoint += 3

        elif splitX[1] == 'X': # Rock
            totaltPoint += 1
            if splitX[0] == 'A': #Rock
                totaltPoint += 3
            elif splitX[0] == 'B': # Paper
                totaltPoint += 0
            else: #Scissor
                totaltPoint += 6
print(totaltPoint)
