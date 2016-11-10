def print_two(*args): 
	arg1, arg2 = args
	print "arg1 : %r \t arg2 : %r" %(arg1,arg2)
''' print_two aka arbitary name
	colon is requirec at the end of the declaration
	intendation (or tab)(or 4 spaces) is required 
		for function body or function definition
'''
def print_two_again (arg1, arg2) :
	print "arg1 : %r \t arg2 : %r" %(arg1,arg2)

def print_none() :
	print "I got nothin...!"

print_two("zed", "Shaw")
print_two_again ("Betz", "Benjz")
print_none()
