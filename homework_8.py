# input numbers until the number <= 0
number = int(input('please enter a number:'))
min_positive_number = number
while number > 0:
    if number < min_positive_number:
        min_positive_number = number
    number = int(input('please enter a number:'))

# print the smallest value
if min_positive_number <= 0:
    print('no positive numbers were inserted.')
else:
    print('smallest value you inserted is' , min_positive_number)

