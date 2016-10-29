# we use %r= raw data = representaion of an object(any obj)
# %r used in ln8,

# here we use string variables within other sting variables
x = 'there are %d types of people' %10
bi = 'binary'
dnt = "don't"
y = 'Those who know %s and those who %s' %(bi,dnt)
# the word don't uses single apostophy but we managed to use it within 
# another string enclosed in single apostrophies 

# printing string within a string
print 'Teacher 1 said : "%r"' %x
print "Teacher 2 said : \"%s\" " %y

nope = False # [this is boolean; not string]
check = "Isn't tha awesome ?! %r"
print check%nope

p = "this is the left side..."
q = "and right of a string"
print p,q # [prints with space between them]
print p+q # [prints without space between them]

r = 50
s = 90
print r,s
print r+s

print """Start
When you want type a lot.
Like if its a big passage.
You can use 3 quotes at the start
and the at the end (dont matter single or double)"""

"""asdfgsdfsdfasdf"""
