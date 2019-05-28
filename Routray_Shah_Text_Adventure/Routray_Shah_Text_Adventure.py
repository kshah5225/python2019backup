from __future__ import print_function
import random
import sys
print ('====================Welcome to our Game====================')

def story():
	'''this inbcludes the entire story'''
	print ('''BACKSTORY: Hi My name is Kakashi. I am a student at the ninja \
academy currently preparing to become a shinobi ninja and protect my \
village from the outside.  The academy is where people train to become a \
shinobi ninja and protect the village, which is called Konoha village. \
I am the top student in the academy right now, as I have trained with my \
father a lot. Currently the village is facing a lot of hardships. Funds are \
currently low and also we are lacking strong shinobi to protect the village. \
I am looking at four different options right now. Choose an option below.''') 
	print ('Choose an option by typing a number and pressing the enter key')
	print ('1)Train with Jiraiya')
	print ('2)Stay and protect the village')
	print ('3)stay in the village and do missions for for the village')
	print ('4)Get trained by Jiraiya but Have to attack other villages')
	answer1 = raw_input('')
	print(' ')
	
	if answer1 == '1':
		print ('''Congratulations you have become very powerful by training \
with Sage Jiraiya. Now on to your next option.''')
		print ('''Type 1 | If you want to go back to the village and help \
carry out missions and protect the village with your life. |''')
		print ('''Type 2 | If you want to stay with Sage Jiraiya and keep \
seeking and training for more power to become extremely powerful and \
hope to achieve a sage rank. |''')
		answer2 = raw_input('')
		print(' ')
		if answer2 == '1':
			print('''The village gets attacked by a giant monkey who tries to \
destroy the village and you save the village by defeating the monkey and then \
become the leader of the village and get recognized for all, but there are \
many tragedies along the way.''')
			print ('''| Game over!!! You went into depression since the monkey \
killed all your friends and family in the village. |''')
			restartornot()
		elif answer2 =='2':
			print('''You learn from the sage Jiraiya and start teaching other \
people training to become very powerful ninjas and become acknowledged by many \
as a very wise sage and also train ninjas to become very powerful and you \
yourself become very powerful.''')
			print('''| RESPECT!!! You have passed this game. You have earned \
the respect of your fellow villagers as a wise sage. |''')
			restartornot()
		else:
			print('''Your indecisiveness has lead to your undoing... you have \
gone insane GAME OVER''')
			restartornot()
	
	elif answer1 == '2':
		print ('''Congratulations you have choose to stay in the village and \
help. Now the village will have more ninja to gaurd the gates from attacks.''')
		print ('''Type 1 | If you want to do deeds for villages. |''')
		print ('''Type 2 | If you want to work as a guard in the village and \
protect the village with your life. | ''')
		answer2 = raw_input('')
		print(' ')
		if answer2 == '1':
			print('''You get paid a lot of money since you have already been \
helping the village and you now you are very wealthy and you have a \
lot of power among the village but are disliked by most of the village.''')
			print('''| Game over!!! You have become wealthy and gained lots of \
power but were never able to achieve your goal of getting acknowledged. |''')
			restartornot()
			
		elif answer2 =='2':
			print('''You are getting paid by the village for going around and \ 
helping people and also work at the village gate where people enter \
and you protect. Life is easy and peaceful for you and you have a \
family and live life with no tragedies.''')
			print('''| RESPECT!!! You have achhieved your goal of being \
aknowledged by the village, and also live a peaceful life and secure the \
village for the future. |''')
			restartornot()
		else:
			print('''Your indecisiveness has lead to your undoing... you have\ 
gone insane GAME OVER''')
			restartornot()
		
	elif answer1 == '3':
		print ('''Congratulations you have became a ninja who only carries out \
missions for the village. You collect lots of funds in the village and \
help the village strive.''')
		print ('''Type 1 | If you want to keep collecting funds and carry out \
missions for the village such as deliver to other villages. |''')
		print ('''Type 2 | If you want to retire in the village and start a \
family and live a happy and peaceful life in the village. |''')
		answer2 = raw_input('')
		print(' ')
		if answer2 == '1':
			print('''The village is striving with money and now are able to \
hire strong shinobi and guardians but you do not have that much \
money and you have no family and have been away from the village \ 
most of the time, and you are acknowledged by the village.''')
			print ('''| RESPECT!!! You have passed this game. You have earned \
the respect of your fellow villagers for your contributions and \
sacrifices. |''')
			restartornot()
		elif answer2 =='2':
			print('''Since you choose to retire the village starts to loose \
money. You get 0 aknowledgment from the village since you retired \
and were not able to help the village.''')
			print ('''| Game over!!! Due to your absence in work the village \
has lost funds and has been shut down and you were never aknowledged. |''')
			restartornot()
		else:
			print('''Your indecisiveness has lead to your undoing... you have \
gone insane GAME OVER''')
			restartornot()
	
	elif answer1 == '4':
		print ('''Congratulations you have became very powerful by training \
with Sage Jiraiya. You are forced to go attack other villages now.''')
		print ('''Type 1 | if you Want to be a target for villages since you \
are extremely strong. |''')
		print ('''Type 2 | If you want to continue carrying out reckless \
missions for the village, but become extremely wealthy and powerful. |''')
		answer2 = raw_input('')
		print(' ')
		if answer2 == '1':
			print('''The Other villages are targeting you for numerous \
assassinations. You are rewarded a lot of respect and get \
acknowldedged by everyone in the village for your contributions.''')
			print('''| RESPECT!!! You have passed this game. You have earned \
the respect of your fellow villagers for your contributions and \
sacrifices. |''')
			restartornot()
		elif answer2 =='2':
			print('''The other villages fear you and you are very powerful as \
a ninja but you stay hidden at all times and you do not get \
acknowledged because no one knows about you and you live a sad \
life but you still gain power.''')
			print ('''| Game over!!! You may have had a lot of money and power \
but no one in the village knew who you were and you were never \
aknowldedged. |''')
			restartornot()
		else:
			print('''Your indecisiveness has lead to your undoing... you have \
gone insane GAME OVER''')
			restartornot()
	else:
		print('''Your indecisiveness has lead to your undoing... you have gone \
insane GAME OVER''')
		restartornot()

def restartornot():
	'''prompts player wheather to restart or not'''
	print('''Type R to restart and E to exit''')
	restartornotvarraw = raw_input('')
	restartornotvar = restartornotvarraw.lower()
	if restartornotvar == 'r':
		story()
	elif restartornotvar == 'e':
		sys.exit()
	else:
		restartornot()
		
story()