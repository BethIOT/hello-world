print "You enter a dark room with 2 doors",
print "Do you go through Door_#1 or Door_#2"

door = raw_input('?? ')

if door=='1':
	print "There's a giant bear eating a cheese cake.",
	print "What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear=raw_input('> ')

	if bear=='1':
		print "The bear eats your face off. Good Job!"
	elif bear=='2':
		print "The bear eats your legs off. Good Job!"
	else :
		print "Well, doing %r is probably better. Bear runs away."%bear
		# This is the only way to win
elif door=='2':
	print "You stare into the endless abyss at Cthulhu's(\"K-thu-lu\") retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input('... ')

	if insanity=='1' or insanity=='2':
		print "Your body survies powered by a mind of Jello. Good Job!"
	else :
		print "The insanity rots your eyes into a pool of muck. Good Job!"
# You cant win if you go through door#2
else:
	print "You stumble around and fall on a knife and die. Good Job!"
# You loose if you dont choose a door.