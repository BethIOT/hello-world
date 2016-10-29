from sys import argv

script, user_name = argv
promt = "# "

print "Hi %s, im the %s script" %(user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s" %user_name
likes = raw_input(promt)
print "Where do you live %s?" %user_name
lives = raw_input(promt)
print "Hey %s, what computer are you working on?" %(user_name)
comp = raw_input(promt)

print """OK, %s
You said %r about liking me
And you live in %r, not sure where that is
And you own a %r computer""" %(user_name, likes, lives, comp)
