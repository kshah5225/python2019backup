'''Procedure'''
#1-4 N/A
#5   int float long
#6   the first one works because both of the inputs have quotes whereas the
#      the second one dosent so basically u need quotes arround all strings
#7   the indexer starts on the first character of a string which can be a space 
#     and marks that letter as 0 and if you go in the + direction then you will 
#     keep counting up until you no longer read any characters but if you input
#     a negative number then you will start at the last character of the string 
#     and count down insted of up
#8   slogan[-4:] will return best
#9   In []: slogan[:10] + 'is awesome!
#    Out[]: 'My school is awesome!
#10  the first comand checks how long the words legenth is and the second one 
#    checks the legenth of the word and gets rid of the last letter
#11  it checks if goo is anyewhere in there like ctrl+f
#12  
def how_eligible(essay):
    '''if essay returns true it has followed instructions to include ?, ", ,, 
    and !.'''
    Rcount=0
    if '?' in essay:
        Rcount = Rcount+1
    if '"' in essay:
        Rcount = Rcount+1
    if ',' in essay:
        Rcount = Rcount+1
    if '!' in essay:
        Rcount = Rcount+1
    return(Rcount)

'''Assignment Check'''
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))
#1   I belive that this worked correctly because you have all four in the first
#    "essay" and one in the other