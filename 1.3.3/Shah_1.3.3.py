from __future__ import print_function # use Python 3.0 printing 
secret = ['red','red','yellow','yellow','black']
'''Procedure'''
#   1-5:N/A

'''Part 1: Conditionals'''
#   6a.True
#   6b.True
#   7.40<x and x<130 and 100<=y and y<=120

'''Part 2: if-else Structures & the print() Function!!!!'''
#   9a:
#       9a. Predictions: 10 output is too young and 16 output is old enough

def age_limit_output(age):
    '''Step 9a if-else example'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
#       Discuss and explain the output
def report_grade(percent):
    '''Step 9b if-else'''
    if percent <= 79:
        print('A grade of' ,percent, 'does not indicate mastery.Seek extra practice or help.')
    if percent >= 85:
        print('A grade of' ,percent, 'percent indicates mastery. Keep up the good work!')
    if percent > 79 and percent < 85:
        print('A grade of' ,percent, 'percent indicates understanding. Try to improve')

'''Part III. The in operator and an introduction to collections'''
#   11
def letter_in_word(guess, word):
    '''returns True if guess is a letter in word and returns False otherwise'''
    if guess in word:
        return True
    else:
        return False
#   12
def hint(color, secret):
    '''The function should print a hint telling whether the color is in string.'''
    
    if color in secret:
        print ('The color' ,color, 'IS in the secret sequence of colors.')
    else:
        print ('The color' ,color, 'IS NOT in the secret sequence of colors.')
        
'''Conclusion'''
#1 if is used to pose a question and if the oi does not return true/ desired value then the next value step is to
#  look at the next elseif which continues on with else if until either the condition is met or you end up at 
#  else which is if all above fails what should I do?
#2 We know if, elif, else, in, and I recently found out you can do while in python
#3 Ira and Kendra have very valid reasons to make it one linme though I think computer power is more important than
#  storage and Jayla's reasoning just dosent make sense as I dont see it anyewhere else but if it were really an issue
#  you can use the find and replace command

'''Assignment Check'''
#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)