import random
'''Procedure'''
#1-3 N/A
'''Part I: Tuples, Syntax'''
#4   (1,43,45,43,345,6,23)
#5   Mr.Brown want headers in multi line comments and answers in single line
#    comments and no logs
#    use upper case for fixed varaibles
#6a  out would be b because it is the second thing in that list
#6b  this would give all values in this listas there are only 3 starting at 0
#7a  this would change 9 to 10 in tuple b
#7b  this would output 9
'''Part II: Lists'''
#8   this will list out all values in the list:values
#9   the first one sets the 2nd position to a string where as the second one asks
#    if some thing is true or false
#10a change the first and second values to said numbers whereas
#10b change result in an error because u cant change a tuple
#11  you are adding strings to integers especially becasue the +5 is not a list
#12  18 b/c 3*6 is 18
'''Part III: Lists and the random module'''
#13 done
#14:
def roll_two_dice():
    '''simulates rolling 2 dice'''
    return (random.randint(1,6)+random.randint(1,6))
'''Conclusion'''
#1  a is a string, b is a tuple, and c is a list
#2  sometimes you need to use a word to be more intutive for both the user and
#   the programmer inseed of having to look up every error code and every
#   response in a lookup book in order to understand the computer
#3  I learned about different ways to interpret data in terms of using if, 
#   while, and in. I also learned when to use tuples, lists and when to use the
#   different data types such as string, long, int, float.
'''Assignment Check'''
#1.3.6 Function Test
print(roll_two_dice())
#  I tried the roll many times and while it seems to be random I was never able 
#  to get 2 sixes(12) so I say that my code works correctly.