from sys import argv
script, file1 = argv

# function to print entire file
def print_all(fl) :
	print fl.read()

# function to go back to start of file
# i.e back to byte 0
def rewind (f1) :
	f1.seek(0)

def print_a_line(line_no, fl) :
	print line_no, fl.readline()

file_now = open(file1)

print "First let's print the whole file \n"
print_all(file_now)

print "Now let's rewind, just like the old tapes"
rewind(file_now)

print "Now I'll show you 3 lines"
scroll = 1
print_a_line(scroll, file_now)
scroll = scroll+1
print_a_line(scroll, file_now)
scroll +=1 # This is how you increment
print_a_line(scroll, file_now)

# Changing the scroll won't jump to that specific line