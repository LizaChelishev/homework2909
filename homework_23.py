# input an integer number
number = int(input('input an integer number:'))
divider = 1
while divider <= number :
    if number % divider == 0:
        print ('Divider is ' , divider)
    divider = divider + 1
