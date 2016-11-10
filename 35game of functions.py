from  sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	print "Enter a number"
	next=raw_input('> ')
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man! Learn to type a number.")
	if how_much<50:
		print "Nice you are not greedy, you win!"
		exit(0)
	else:
		dead("You greed theif! You're gonna die")

def bear_room():
	print "There is a bear here. The bear has a pot of honey"
	print "The bear is in front of a room. How are you going to move the bear?"
	bear_moved=False
	query=0
	while True:
		next = raw_input('> ')
		if query>=2 :
			dead('The bear comes and knocks you out cold while u contemplate your move')
		elif next == "take honey":
			dead("The bear looks at you and slaps your face off.")
		elif next=="taunt bear" and not bear_moved:
			bear_moved=True
		elif next=="taunt bear" and bear_moved:
			dead("The bear gets pissed and chews your leg off.")
		elif next=="open room" and bear_moved:
			gold_room()
		elif next=="i dont know" or next=="what do i do" or next=="what am i to do":
			print "You could 'take honey'"
			print "Or else you could 'taunt bear'"
			print "Or you could just go shead and 'open room'"
			query+=1
		else:
			print "I have no ides what %r means"%next

def hell_room():
	print "You now stand before the dDemon Lucifer"
	print "He stares at you and you go insane"
	print "Do you flee for your life or eat you head?"
	next=raw_input('> ')
	if "flee" in next or "run" in next:
		#This looks at the text and if the keyword 'flee' is there in it
		start()
	elif "head" in next:
		dead("That was tasty")
	else:
		hell_room()

def dead(why):
	print why, "Good Job.!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door on your left and your right."
	print "Which one do you take?"
	next=raw_input("> ")
	if next=="left":
		bear_room()
	elif next=='right':
		hell_room()
	else:
		dead('You stumble around in the dark and fall and break your head')

start()
# The program has only this one statement