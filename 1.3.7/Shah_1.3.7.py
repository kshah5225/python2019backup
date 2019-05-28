from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

'''Procedure'''
#1-3
'''Part I: for loops, range(), and help()'''
#4
def days():
    ''' Explain the function here
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')
        
def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks2')
#5
def dice(n):
    randlist = []
    randcount = 0
    while randcount < n:
        randlist.append(random.randint(1,6))
        print (randlist)
        randcount = randcount + 1
    plt.hist(randlist, bins = [1,2,3,4,5,6])
    plt.savefig("1.3.7/new_piks.png")
    return (sum(randlist))

def roll_hundred_pair():
    dice_roll_list = dice(100)
    return dice_roll_list

'''Part II: While loops'''
#7   line 2 is nessecary because if you set the guess to a value when u re run 
#    this code it will use the same value used as last time
def validate():
    guess = '1' # initialization with a bad guess so loop starts
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
#8
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 
    # prints wheather choosen person won lottery
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # keeps running until the legenth of the 
    #index is gone through
        print(p+', ', end='')
    print(players[len(players)-1]) # prints how many players are still in?
    #check if person won or not
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses
#9
def goguess():
    '''try to guess the raanadon number given gigiven hints in the least amount of
guesses'''
    randnumbergoguess = random.randint(0,20)
    goguessguess = 21
    guessescount = 0
    while int(goguessguess) != int(randnumbergoguess):
        goguessguess = raw_input()
        guessescount = guessescount + 1
        if int(goguessguess) < int(randnumbergoguess):
            print ('', goguessguess ,' is too low')
        elif int(goguessguess) > int(randnumbergoguess):
            print ('', goguessguess ,' is too high')
    return print('You guessed in', guessescount, 'guesses!')
#10   you need 12 trys becauseif you choose in the middle every time then you 
#     will know to go up or down and that will allow you to narrow in on your
#     target quicker
'''Part III: Practice'''
#11a
def matches(ticket, winners):
    '''find out how many of your lottery ticket numbers are correct'''
    numberscorrect = 0
    if winners.count(ticket[0]) >0:
        numberscorrect = numberscorrect + 1
    if winners.count(ticket[1]) >0:
        numberscorrect = numberscorrect + 1
    if winners.count(ticket[2]) >0:
        numberscorrect = numberscorrect + 1
    if winners.count(ticket[3]) >0:
        numberscorrect = numberscorrect + 1
    if winners.count(ticket[4]) >0:
        numberscorrect = numberscorrect + 1
    print (numberscorrect)
    return numberscorrect
#11b
def report(guess, secret):
    '''find out how many of your mastermind guesses are right'''
    numberscorrectinplace = 0
    checkstep = 0
    while len(guess) > checkstep:
        if guess[checkstep] == secret[checkstep]:
            numberscorrectinplace = numberscorrectinplace + 1
        checkstep = checkstep + 1
    checkstep = 0
    numberscorrecteverywhere = 0
    while len(guess) > checkstep:
        if guess[checkstep] in secret:
            numberscorrecteverywhere = numberscorrecteverywhere +1
        checkstep = checkstep + 1
    print(numberscorrectinplace, numberscorrecteverywhere)
    
'''Conclusion'''
#1   it is harder to interpret and takes up more bytes. It can also get stuck
#    in loop easier
#2   in itiration you go everything step by step one at a time.
#3   they are very similar and can always be used interchangeably but for loop
#    is better at things that need itteration
#4   We didnt really work together all that much because I finished this by
#    myself as it says it is due tonight monday so I didnt get the time to work
#    on this with my partner.

'''Assignment Check'''
#1.3.7 Function Test
roll_hundred_pair()
goguess()
goguess()
print('next 4 lines should be 2,3,2,3')
matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17])
matches([11, 12, 13, 14, 15], [11, 8, 12, 15, 17])
report(['red','red','red','green','yellow'], ['red','red','yellow','yellow','black'])
report(['red','blue','red','green','yellow'], ['red','blue','yellow','yellow','yellow'])
#    based on this I get the correct reasults leading me to belive that my
#    method is correct