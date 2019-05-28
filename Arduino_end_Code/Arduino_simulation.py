from __future__ import print_function
import random
import sys

current_id_number = '0'
ID_List = []
while (1==1):
    print('''Enter your id number now''')
    current_id_number = raw_input('')
    if (current_id_number == 'Done'):
        file = open('testfile.txt','w+')
        file.write(str(ID_List))
        file.close()
        ID_List = ()
        break
    ID_List += [int(current_id_number)]
    print(ID_List)