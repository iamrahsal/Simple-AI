
print ("Sidi: Hey, Who are you?")
usrname = input()
print ("Sidi: Welcome " + usrname )

while (True):
	userInp = input()
	if (userInp in ['hi','Hi','HI']):
		print ("Sidi: Hello")
		userInp = ""
	elif (userInp in ["How are you","how are you","How are you?","how are you?"]):
		print ("Sidi: I am fine " + usrname )
		userInp = ""
		userInp = input("Sidi: What about you dear?\n")
		print ("Sidi: That's good :-) ")
		print ("Sidi: Tell me something " + usrname + "..")
	elif (userInp in ['I LOVE YOU','I love you','i love you']):
		print ("Sidi: Love you too " + usrname + ":-)")
		userInp = ""
	elif (userInp in ['See you later','see you later','c u later','SEE YOU LATER']):
		print ("Sidi: Ok " + usrname + ". As your wish.")
		userInp = ""
	else:
		print ("Sidi: I don't understand what you said")