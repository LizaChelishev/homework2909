# input numbers until the number <= 0
max_positive_number = 0
number = int(input('please enter a number:'))
while number > 0:
    if number > max_positive_number:
        max_positive_number = number
    number = int(input('please enter a number:'))

# print the highest value
if max_positive_number == 0:
    print('no positive numbers were inserted.')
else:
    print('highest value you inserted is' , max_positive_number)

