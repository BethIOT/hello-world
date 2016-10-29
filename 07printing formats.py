print #prints blank line
print "#" *10
print "$" *20
print "@" *30
print

ch1  = 'C'
ch2  = 'h'
ch3  = 'e'
ch4  = 'e'
ch5  = 's'
ch6  = 'e'
ch7  = 'B'
ch8  = 'u'
ch9  = 'r'
ch10 = 'g'
ch11 = 'e'
ch12 = 'r'

print "With comma : ",
print ch1+ch2+ch3+ch4+ch5+ch6,
print ch7+ch8+ch9+ch10+ch11+ch12
print "Without comma : "
print ch1+ch2+ch3+ch4+ch5+ch6
print ch7+ch8+ch9+ch10+ch11+ch12
print "With plus : "
print ch1+ch2+ch3+ch4+ch5+ch6+
print ch7+ch8+ch9+ch10+ch11+ch12
print


# %r can read reany format. mainly used for debugging
pattern = "%r %r %r %r"

print pattern%(1,2,3,4)
print pattern%('one', "two", 'three', "four")
print pattern%(True, False, True, False)
print pattern%(pattern,pattern,pattern,pattern)
print pattern%(
	"i had this thing",
	'that you could type up right',
	"but it didnt sing",
	'so i said goodnight')
# you could continue a command into the next line if the
# previous one ends with a ( or,
