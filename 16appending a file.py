from sys import argv
script, file = argv

# filename must be included. if doing the write/append operation
# a new file will be created if 'filename' doesnt exist

print "We are going to erase %r" %file
print "Ctrl+c to Cancel \t Enter to Proceed"
raw_input('?? ')

print "Opening the file...."
operate = open(file,"a+")
# see pydoc for more details
# w=wrie ; a=append ; r=read(default)
# r+ = read and write
# w+ = write and read

print "This is whats in the file \n", operate.read()
operate.seek(0)
# operate.close()

# operate = open(file,"a+")

print "Truncating the file"
print "I need you to type 3 lines."
line1 = raw_input('L1: ')
line2 = raw_input('L2: ')
line3 = raw_input('L3: ')


print "OK, So.... Now I'm going to write these to the file %r and this is %r " %(file,line1)
operate.write('\n')
operate.write(line1)
operate.write('\n')
operate.write(line2)
operate.write('\n')
operate.write(line3)
operate.write('\n')

print "And finally I got to close this file"
operate.close()
