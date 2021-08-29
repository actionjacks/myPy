import random
from random import randint

mylisy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylisy:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd nuber: {num}')

#################################

myList = [(1, 2), (3, 4), (5, 6), (7, 8)]
for i in myList:
    print(i)

for (a, b) in myList:
    print(f'{a} this is first element')

###################################

d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(value)

#########while loop#################
x = 0

while x < 5:
    print(f'value {x}')
    x += 1
else:
    print('stop loop')

# break finish the loop
# continue go to closes enclosing loop
# pass does nothing at all

mystring = 'jacek'
for letter in mystring:
    if letter == 'c':
        continue  # go to top of the loop
    print(f'letter is {letter}')

#
# first is default null
# range(3,10) start at index 3 up to 10
# range(0,20,2) start at index 0 up to 20 step 2
for num in range(10):
    print(num)

mygeneratedlist = list(range(5))
print(mygeneratedlist)

#
index_count = 0
# for letter in 'abcdefg':
#     print('at index {} the letter is {}'.format(index_count, letter))
#     index_count += 1
for letter in 'abcdefg':
    print(f'at index {index_count} the letter is {letter}')
    index_count += 1

# enumetator
mySomeLetters = 'aasdfghjkl'

for index, letter in enumerate(mySomeLetters):
    print(index)
    print(letter)
    print('\n')

firstlist = [1, 2, 3]
secondlist = ['a', 'b', 'c']
for item in zip(firstlist, secondlist):
    print(item)

e = {'key': 333}
print(333 in e.values())  # true

ordererlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(ordererlist)
print(ordererlist)

somerandomInt = randint(0, 100)
print(somerandomInt)

mystring = 'jacek placek'
mylistwhitstrig = [letter for letter in mystring]  # append letter to new list
print(mylistwhitstrig)

mynumberlist = [num**2 for num in range(0, 10)]
print(mynumberlist)

mynumberlist2 = [num for num in range(0, 10) if num % 2 == 0]
print(mynumberlist2)
#
celcius = [0, 10, 20, 34.5]

fahrenheit2 = []
for temp in celcius:
    fahrenheit2.append(((9/5)*temp+32))
# same
fahrenheit = [((9/5)*temp+32)for temp in celcius]
print(fahrenheit)

# can do if statements
results = [x if x % 2 == 0 else 'odd' for x in range(0, 11)]
print(results)

list3 = []
for x in [2, 5, 6]:
    for y in [100, 200, 300]:
        list3.append(x*y)
print(list3)
# same
mylist4 = [x*y for x in [2, 5, 6] for y in [100, 200, 300]]
print(mylist4)

# tests quess game


print('\n')
randomInt = randint(1, 100)
print('############# Quess the number between 1 and 100 ##############')

guesses = []
playerQuess = 0

print('## debug random number is', randomInt)

while playerQuess != randomInt:
    playerQuess = int(input())
    guesses.append(playerQuess)

else:
    print('U WON')
