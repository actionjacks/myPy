st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word.startswith('s'):
        print(word)
# or
for word in st.split():
    if word[0].lower() == 's':
        print(word)

# -----------------------------
evenNumbers = range(0, 10)
for number in evenNumbers:
    if number % 2 == 0:
        print(f'even {number}')
# or
for num in range(0, 11, 2):
    print(num)

# -----------------------------
dicisible = [x if x % 3 == 0 else '-' for x in range(1, 50)]
print(dicisible)
# or
dicisible2 = [x for x in range(1, 51)if x % 3 == 0]

# -----------------------------

st2 = 'Print every word in this sentence that has an even number of letters'

for word in st2.split():
    if len(word) % 2 == 0:
        print(word)

# -----------------------------
listOfNumbers = range(1, 100)
for number in listOfNumbers:
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        pass

# -----------------------------

st3 = 'Create a list of the first letters of every word in this string'
firstletterList = []
for i in st3.split():
    firstletterList.append(i[0])

print(firstletterList)
# or
print([word[0] for word in st3.split()])
# -----------------------------
