# input an integer number
number = int(input('input an integer number:'))
digit = number % 10
reminder = number // 10
while reminder >= 10:
    digit = digit + reminder % 10
    reminder = reminder // 10

print ('The sum of digits is: ', digit+reminder)
