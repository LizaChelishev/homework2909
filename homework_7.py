
# input numbers until the number <= 0
number = int(input('please enter a number:'))
list= []
while number > 0:
    number = int(input('please enter a number:'))

# print the highest value
    list.append(number)

print(list)
print('highest value you inserted is' , max(list))

