from __future__ import print_function # use Python 3.0 printing 
'''Part I. Nested if structures and testing'''
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a      line 17
#1bi     orange
#1bii    apple
#1biii   potato
#1biiii  literally anything else other than what is in the list
#1c      because the if astatement is for fruits and the else is not friuts
#2:
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print("works")
        return False
#3:
def f(n):
    if int(n)==n:
        if n%2==0:
            if n%3==0:
                print('', n ,' is a multiple of six')
                return 'n is a multiple of six'
            else:
                print('', n ,' is even')
                return 'n is even'
        else:
            print('', n ,' is odd')
            return 'n is odd'
    else:
        print('', n ,' is not a integer')
        return 'n is not a integer'
#4 3.3, 5, 2, 24
#5:
def f_test():
    ''' Unit test for f(n)
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if f(3.3) !='n is not a integer':
        works = 'not an integer bug in f(n)'
    if f(5) != 'n is odd':
        works = 'odd detection bug in f(n)'
    if f(2) != 'n is even':
        works = 'even detection bug in f(n)'
    if f(24) != 'n is a multiple of six':
        works = 'multiple of 3 detection bug in f(n)'
    # Add tests so that all lines of code are visited during test
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
'''Part II: The raw_input() function, type casting, and print() from Python 3'''
#8:
import random
def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess == secret:
        print('Right on! my number is', guess, end='!\n')
    elif secret > guess:
        print('Too low - my number is ', secret, '.', sep='')
    elif secret < guess:
        print('Too high - my number is ', secret, '.', sep='')
    else:
        print('error')
#9aif you dont have the end then the ! will(not 100% sure)end up on another line
def quiz_decimal(low, high):
    print('Type a number between ', low , 'and', high,':')
    guess = raw_input('Guess: ')
    if guess < high:
        print('No,', guess ,'is greater than', high ,)
    elif guess > low:
        print('No,', guess ,'is less than', low ,)
    else:
        print('Good!', low ,'<', guess ,'<', high ,)
        
'''Conclusion'''
#1 an if statement runs the senario of something being put into a certian
#    process and checking if that process spit out the correct/expected value
#2 an infinite amount if you use functions but only 5 times without functions
#3 if they have a test suite they can test after every change to make sure they
#    are improving without breaking something old insted of testing every 
#    individual aspect every time they make a change
#4 Yes you can though it would be impractical in this small of a program
    
'''Challenge'''
def is_it_an_integer(n):
    '''is it a integer'''
    if int(n)==n:
        is_it_even(n)
    else:
        print('', n ,' is not a integer')
        return 'n is not a integer'
def is_it_even(n):
    '''is it even'''
    if n%2==0:
        is_n_divisible_by_3(n)
    else:
        print('', n ,' is odd')
        return 'n is odd'
def is_n_divisible_by_3(n):
    '''is it divisible by 3'''
    if n%3==0:
        print('', n ,' is a multiple of six')
        return 'n is a multiple of six'
    else:
        print('', n ,' is even')
        return 'n is even'
    
def funconfunc(n):
    '''challenge function'''
    
def f_challenge(number):
    '''returns all possible results from the flow chart provided in question 3 
    from the activity'''
    is_it_an_integer(number)

'''Assignment Check'''
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)
#1 I did he assignment correctly and I know this because I got all good! twice,
#  once for the f_test and once for the fruit function test