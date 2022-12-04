path =  r'./input1.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

totaltPoint = 0

for x in my_list:
    splitX = x.split(' ')
    if len(splitX) == 2:

        if splitX[1] == 'Y': # Draw
            if splitX[0] == 'A': # Rock
                totaltPoint += 4
            elif splitX[0] == 'B': # Paper
                totaltPoint += 5
            else: # Scissor
                totaltPoint += 6
        
        elif splitX[1] == 'Z': # Win
            if splitX[0] == 'A': #Rock
                totaltPoint += 8
            elif splitX[0] == 'B': #Paper
                totaltPoint += 9
            else: #Scissor
                totaltPoint += 7

        elif splitX[1] == 'X': # Lose
            if splitX[0] == 'A': #Rock
                totaltPoint += 3
            elif splitX[0] == 'B': # Paper
                totaltPoint += 1
            else: #Scissor
                totaltPoint += 2
print(totaltPoint)
