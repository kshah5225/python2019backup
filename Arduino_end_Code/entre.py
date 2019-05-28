NewID_List = []
file = open('testfile.txt', 'r') 
NewID_List = file.read()
print NewID_List

fileperm = open('Arduino_end_Code/All_ID_numbers.txt', 'r') 
permID_List = fileperm.read()
file.close()
print permID_List

permID_List += NewID_List


fileperm = open('All_ID_numbers.txt','w+')
fileperm.write(NewID_List)
