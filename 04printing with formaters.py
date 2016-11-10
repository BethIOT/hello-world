# Use of %s=string and %d=decimal
name = 'Bethsay'
age = 24
height=172
weight = 75
eyes = 'black'
teeth = 'white'
hair = 'black'

print "I am", name
print "I am %s" %name 
print "I am",age,"years old"
print "I am %d years old" %age
print "I am %d cms tall and %d kgs heavy" %(height, weight)
print "i got %s eyes, %s teeth and %s hair" %(eyes,teeth,hair)
print "if i add %d %d %d, we get %d" %(age, weight, height, age+weight+height)

print "No. of charecters in your name", len(name)
print "Name in all upper case", "betz".upper()
print "Name in all lower case", name.lower()
# str(variable) will convert variable to a string