#! /usr/bin/env python

import os
import sys


def survey():
    # Read in the first name of the employee
    print("What is your full name?: ")
    full_name = sys.stdin.readline()

    # Create id
    names = full_name.split(' ')
    id = names[0][0] + names[1][0:5]

    # Get email
    print("What is your email? ")
    email = sys.stdin.readline()

    return ( full_name, id, email )

# Summary function
def summary( full_name, email ):
    while True:
        print("Is this information correct?\nFull Name: {}\nEmail: {}".format(full_name, email) )
        ans = sys.stdin.readline()
        if ans.ascii_lowercase() is 'y' or ans is 'yes':
            return True
        elif ans.ascii_lowercase() is 'n' or ans is 'no':
            return False
        print("I'm sorry, that was not valid input")
    
# Main
correct = False
# Program loop
while correct is False:
    data = survey()
    # Give summary
    correct = summary( data[0], data[2] )
print("This is your id, write it down somewhere you will remember")
sys.stdout.write(data[1])
