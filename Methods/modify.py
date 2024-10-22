# print('Starting list:')
fruit = ['apple','banana', 'orange']
print(fruit)
print('----------------------------')

# This will MODIFY [0] apple > gala apple
fruit[0] = 'gala apple'
# This will MODIFY [2] orange > cherry
fruit[2] = 'cherry'

print('Modified list [0] apple to gala apple:')
print(fruit)
print('----------------------------')

# Add, or APPEND, element to end of list
fruit.append('pineapple')

print('Adding a pineapple to end of list:')
print(fruit)
print('----------------------------')

# INSERT lemon after gala apple:
fruit.insert(1, 'lemon')
print(fruit)


# starting with empty list []
dairy = []

dairy.append('milk')
dairy.append('yogurt')
dairy.append('swiss cheese')

print('Build dynamic list:')
print(dairy)