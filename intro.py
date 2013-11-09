# Welcome! This is a Python program file

# The lines that start with a hash (#) are comments
# They are for you to read and are ignored by Python

# When you see 'GO!', save and run the file to see the output
# When you see a line starting with # follow the instructions
# Some lines are python code with a # in front
# This means they're commented out - remove the # to uncomment
# Do one challenge at a time, save and run after each one!

# 1. This is the print statement

print("Hello world")

# GO!

# 2. This is a variable

message = "Level Two"

# Add a line below to print this variable

# GO!

# 3. The variable above is called a string
# You can use single or double quotes (but must close them)
# You can ask Python what type a variable is. Try uncommenting the next line:
# print(type(message))
# GO!

# 4. Another type of variable is an integer (a whole number)
a = 123
b = 654
c = a + b

# Try printing the value of c below to see the answer
# GO!

# 5. You can use other operators like subtract (-) and multiply (*)
# Try some below by replacing the word with the correct operator

# a times b
# b minus a
# 12 times 4
# 103 add 999

# GO!

# 6. Variables keep their value until you change it

a = 100
# print(a)  # think - should this be 123 or 100?

c = 50
# print(c)  # think - should this be 50 or 777?

d = 10 + a - c
# print(d)  # think - what should this be now?

# GO!

# 7. You can also use '+' to add together two strings

greeting = 'Hi '
name = ''  # enter your name in this string

message = greeting + name
# print(message)

# GO!

# 8. Try adding a number and a string together and you get an error:

# age =  # enter your age here (as a number)

# print(name + ' is ' + age + ' years old')

# GO!

# See the error? You can't mix types like that.
# But see how it tells you which line was the error?
# Now comment out that line so there is no error

# 9. We can convert numbers to strings like this:

# print(name + ' is ' + str(age) + ' years old')

# GO!

# No error this time, I hope?

# Or we could just make sure we enter it as a string:

# age =  # enter your age here, as a string

# print(name + ' is ' + age + ' years old')

# GO!

# No error this time, I hope?

# 10. Another variable type is called a boolean
# This means either True or False

raspberry_pi_is_fun = True
raspberry_pi_is_expensive = False

# We can also compare two variables using ==

bobs_age = 15
# your_age =  # fill in your age

# print(your_age == bobs_age)  # this prints either True or False

# GO!

# 11. We can use less than and greater than too - these are < and >

# bob_is_older = bobs_age > your_age

# print(bob_is_older)  # do you expect True or False?

# GO!

# 12. We can ask questions before printing with an if statement

money = 500
phone_cost = 240
tablet_cost = 200

total_cost = phone_cost + tablet_cost
can_afford_both = money > total_cost

if can_afford_both:
    message = "You have enough money for both"
else:
    message = "You can't afford both devices"

# print(message)  # what do you expect to see here?

# GO!

# Now change the value of tablet_cost to 260 and run it again
# What should the message be this time?

# GO!

# Is this right? You might need to change the comparison operator to >=
# This means 'greater than or equal to'

raspberry_pi = 25
pies = 3 * raspberry_pi

total_cost = total_cost + pies

if total_cost <= money:
    message = "You have enough money for 3 raspberry pies as well"
else:
    message = "You can't afford 3 raspberry pies"

# print(message)  # what do you expect to see here?

# GO!

# 13. You can keep many items in a type of variable called a list

colours = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# You can check whether a colour is in the list

# print('Black' in colours)  # Prints True or False

# GO!

# You can add to the list with append

colours.append('Black')
colours.append('White')

# print('Black' in colours)  # Should this be different now?

# GO!

# You can add a list to a list with extend

more_colours = ['Gray', 'Navy', 'Pink']

colours.extend(more_colours)

# Try printing the list to see what's in it

# GO!

# 14. You can add two lists together in to a new list using +

primary_colours = ['Red', 'Blue', 'Yellow']
secondary_colours = ['Purple', 'Orange', 'Green']

main_colours = primary_colours + secondary_colours

# Try printing main_colours

# 15. You can find how many there are by using len(your_list). Try it below

# How many colours are there in main_colours?

# GO!

all_colours = colours + main_colours

# How many colours are there in all_colours?
# Do it here. Try to think what you expect before you run it

# GO!

# Did you get what you expected? If not, why not?

# 16. You can make sure you don't have duplicates by adding to a set

even_numbers = [2, 4, 6, 8, 10, 12]
multiples_of_three = [3, 6, 9, 12]

numbers = even_numbers + multiples_of_three
# print(numbers, len(numbers))
numbers_set = set(numbers)
# print(numbers_set, len(numbers_set))

# GO!

colour_set = set(all_colours)
# How many colours do you expect to be in this time?
# Do you expect the same or not? Think about it first

# 17. You can use a loop to look over all the items in a list

my_class = ['Sarah', 'Bob', 'Jim', 'Tom', 'Lucy', 'Sophie', 'Liz', 'Ed']

# Below is a multi-line comment
# Delete the ''' from before and after to uncomment the block

'''
for student in my_class:
    print(student)
'''

# Add all the names of people in your group to this list

# Remember the difference between append and extend. You can use either.

# Now write a loop to print a number (starting from 1) before each name

# 18. You can split up a string by index

full_name = 'Dominic Adrian Smith'

first_letter = full_name[0]
last_letter = full_name[19]
first_three = full_name[:3]  # [0:3 also works]
last_three = full_name[-3:]  # [17:] and [17:20] also work
middle = full_name[8:14]

# Try printing these, and try to make a word out of the individual letters

# 19. You can also split the string on a specific character

my_sentence = "Hello, my name is Fred"
parts = my_sentence.split(',')

# print(parts)
# print(type(parts))  # What type is this variable? What can you do with it?

# GO!

my_long_sentence = "This is a very very very very very very long sentence"

# Now split the sentence and use this to print out the number of words

# GO! (Clues below if you're stuck)

# Clue: Which character do you split on to separate words?
# Clue: What type is the split variable?
# Clue: What can you do to count these?

# 20. You can group data together in a tuple

person = ('Bobby', 26)

# print(person[0] + ' is ' + str(person[1]) + ' years old')

# GO!

# (name, age)
students = [
    ('Dave', 12),
    ('Sophia', 13),
    ('Sam', 12),
    ('Kate', 11),
    ('Daniel', 10)
]

# Now write a loop to print each of the students' names and age

# GO!

# 21. Tuples can be any length. The above examples are 2-tuples.

# Try making a list of students with (name, age, favourite subject and sport)

# Now loop over them printing each one out

# Now pick a number (in the students' age range)
# Make the loop only print the students older than that number

# GO!

# 22. Another useful data structure is a dictionary

# Dictionaries contain key-value pairs like an address book maps name
# to number

addresses = {
    'Lauren': '0161 5673 890',
    'Amy': '0115 8901 165',
    'Daniel': '0114 2290 542',
    'Emergency': '999'
}

# You access dictionary elements by looking them up with the key:

# print(addresses['Amy'])

# You can check if a key or value exists in a given dictionary:

# print('David' in addresses)  # [False]
# print('Daniel' in addresses)  # [True]
# print('999' in addresses)  # [False]
# print('999' in addresses.values())  # [True]
# print(999 in addresses.values())  # [False]

# GO!

# Note that 999 was entered in to the dictionary as a string, not an integer

# Think: what would happen if phone numbers were stored as integers?

# Try changing Amy's phone number to a new number

# addresses['Amy'] = '0115 236 359'
# print(addresses['Amy'])

# GO!

# Delete Daniel from the dictinary

# print('Daniel' in addresses)  # [True]
# del addresses['Daniel']
# print('Daniel' in addresses)  # [False]

# GO!

# You can also loop over a dictionary and access its contents:

'''
for name in addresses:
    print(name, addresses[name])
'''

# GO!

# 23. A final challenge using the skills you've learned:
# What is the sum of all the digits in all the numbers from 1 to 1000?

# GO!

# Clue: range(10) => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Clue: str(87) => '87'
# Clue: int('9') => 9
