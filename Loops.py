# While Loop
# example
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

# example
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

    # Break and Continue - Part 1
    count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

    # For Loop
    # example 
    numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
    # For loop with string
    language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

    # Nested For Loop
    person = {
    'first_name': 'Abdulkadir',
    'last_name': 'Mohamud',
    'age': 250,
    'country': 'The Netherlands',
    'is_not _married': True,
    'skills': ['JavaScript', 'React', 'Node',  'SQL', 'MongoDB', 'Python'],
    'address': {
        'street': 'istrakova street',
        'zipcode': '03210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

            # For Else
            for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

    