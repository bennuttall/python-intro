# Guessing Game

from random import choice

answer = choice(range(1, 21)) #randomly select a number between 1 and 20

guess = raw_input('What is your guess? ')

### 1. Now make it tell them if they guessed right
'''
    Think - if you just copied the block of code 3 times, what if the
    number of attempts was 100 - would you still copy and paste?

    Try something smart like a loop
'''

### 2. Now make it give them 3 guesses
'''
    Think - what's the best way to keep count?
'''

### 3. Now make it tell them if their guess was too high or too low

### 4. Now make it tell them how many guesses they have left
'''
    Think - how can you calculate this?
    Is there an easier way to keep track?
'''

### 5. Now change it so they have 5 guesses
'''
    Think - could you have written it better so that changing the number
    of guesses was easier?
    
    If you had that number written more than once, how could you change it
    to be easier to update in future?
'''

### 6. Are there any bugs?
'''
    What happens when they get it right? Does the game end?
    What happens when they get it wrong 5 times? Does the game end?
    What happens if they enter something that's not a number?
'''
