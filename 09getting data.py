print "How old are you?",
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
# the comma makes sure that the text teh user types stays on the same
# line as that of the question
print '''So you're %r years old
\t%r feet tall and
\t%r kgs heavy''' % (age, height, weight)
print ("You are %r years old"
"%r feet tall and"
"%r kgs heavy") %(age, height, weight)
