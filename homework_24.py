# input an integer number
number1 = int(input('input the first integer number:'))
number2 = int(input('input the second integer number:'))
divider = 1
biggest_common_divider = 1
while divider <= min(number2, number1):
    if (number1 % divider == 0) and (number2 % divider == 0):
        biggest_common_divider = divider
    divider = divider + 1
print('The largest common divider is ', biggest_common_divider)
