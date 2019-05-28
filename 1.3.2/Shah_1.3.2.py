'''Part 1: Numeric types'''
# 7. a.the float gives an number that is real but not an integer while the int gives an integer
# 7. b.returns rounded down integer value(no decimals)
# 9.35834136918934220777541995677272642015423987712183913488967L
'''Part 2: Function Definitions'''
def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
# 11.ipython is for debugging and testing while mthe file is for a final product and final testing
# 12.behind the scenes they used parenthesis but in visual blocks they used wrapping blocks
# 13.so users other then you can get help if needed
# 14.reduce ram usage and lagg over time
# 15.a compile would translate the entire thing at once
# 16: a&b
def hyp(leg1, leg2):
    import math
    return math.sqrt(((leg1)**2)+((leg2)**2))
#16. c:
def perimeter(base, height):
    return (((base)*2)+((height)*2))
    
def mean(first, second, third):
   return((first+second+third)/3.)

'''Conclusion'''
#1.A machine that automatically buys a certian shirt from supreme at 8
#2.
#  float - any real number,
#  int - any real number rounded down to the closest integer,
#  boolean(already knew) - true or false,
#  string - any combination of characters
#3.in i python it dosent record data and you cannot make a function to call upon 
#  and in a text python file you can make a saveable file and edit it insted of 
#  having to log to save and here you can uses log more effectivly
#4.if you put something in a function then you can repeat a set of things without 
#  having to retype them which makes code a ton shorter
#5.for some reason my code is giving me an error on a comment line and isnt even 
#  reaching the copy pasted line of code but I suspect that the functions should 
#  have un and I should have gotten the answers throught the functions
#  (yes I did save but that didnt fix the problem)
#  NEW:It fixed in the computer room and it now works and it shows all the answers to 
#  the previous problems except it donent show the 2nd add tip
#1.3.2 Function Test
print add_tip(20,0.15)
print add_tip(30,0.15)
print hyp(3,4)
print mean(3,4,7)
print perimeter(3,4)