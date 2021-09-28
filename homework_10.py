# input an integer number
number = int(input('input an integer number:'))
digit = number // 10
while digit >= 10:
    digit = digit // 10
print (digit)
