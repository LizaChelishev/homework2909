# input an integer number
number = int(input('input an integer number:'))
if number == 0:
    factorial = 1
else:
    factorial = number
while number > 1:
    factorial = factorial * (number - 1)
    number = number -1

print ('Factorial ',  factorial)
