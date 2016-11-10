the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'bananas']
coins = [1,2,5,'pennies', 'quarters', 'dimes', 'nickles']

# In python these are called "lists".
# In other languages they are called "arrays".

for i in the_count: # numbers only
	print "This is the count %d" %i
for fr in fruits: # strings only
	print "A fruit of type %s" %fr
for c in coins: #mixed list 
	print "I got %r"%c
# fruit loop wont print quotes but coin loop will
# they say %r wont always behave as we expect

# This is how to build a list
new=[] #empty list
for x in range(0,10):
	"""Start of range is inclusive
	End is exculsive
	tarting from 0 is default, so this can be written as range(6)
	You can also specify if incrment or decrement
	You can also specify step size """
####>> range(start, end, step)
	print "Adding %d to the list" %x
	new.append(x)
	# append is a built-in function

for n in new:
	print "The data is : %r" %n

#Another way to build a list
new2=range(6)
for i in new2:
	print "List2 items %d"%i
for t in range(6):
	print "%d"%t

