#!/usr/bin/env python3
# _*_ coding: UTF-8 _*_
"""
number_guess - Number guessing game
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Guess a number between 0 and 100.
This example illustrates while-loop with boolean flag, nested-if, 
and random module.

Usage: number_guess.py
"""

import random       # Using random.randint()

# Set up a secret number between 0 and 99
secret_number = random.randint(0,100) # retrun a random int between 0 and 100.
trial_number = 0        # number of trials
done = False        # bool flag for loop control

while not(done):
    trial_number += 1
    number_in = (int)(input('Enter your guess (betwen 0 and 100):'))
    if number_in == secret_number:
        print('Congratulation!')
        print('You got it in {} trials.'.format(trial_number)) # Fromatted printing
        done = True
    elif number_in < secret_number:
        print('Try higger...')
    else:
        print('Try lower...')
