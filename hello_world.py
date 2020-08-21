happy_ness = input('How happy are you today on a scale from 1-10? ')
if int(happy_ness) in range(1,5):
	print('Get some coffee bro!')
elif int(happy_ness) in range(5,10):
	print('Keep crunching!')
else:
	print('What about a scale from 1-10 did you not understand?')
