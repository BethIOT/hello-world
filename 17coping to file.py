from sys import argv
from os.path import exists
""" os.path is used so that python can accept
	different OS specific path formats.
	exists return a boolean depending if the
	specified path is true or false"""

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)
in_file = open(from_file)
in_data = in_file.read()
# in_data = open(from_file).read()

print "The file is %d bytes long" %len(in_data)

print "Does the file exist.?", exists(to_file)
print "Hit Enter to continue ; Ctrl+c to quit"
raw_input ("> ")

out_file = open(to_file, 'w')
out_file.write(in_data)

print "The job is done"
out_file.close()
in_file.close() # omit this line
# if "in_data = open(from_file).read()" was used

# one line version of this whole program
# from sys import argv ; from os.path import exists ; script, from_file, to_file = argv ; in_data = open(from_file).read() ; out_file = open(to_file, 'w') ; out_file.write(in_data) ; out_file.close()
