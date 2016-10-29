from sys import argv
script, filename = argv

text=open(filename)
# Any file that we have to operate, 
#1 is first opened, 
#2 then operatd on it
#3 and finally closed

print "Here's your file %r : " %filename
print text.read()
# The varible text is now an obect.'.' is used to perform function on an object
print "Type a file name : "
file2 = raw_input('# ')
text2= open(file2)
print text2.read()

text.close()
text2.close()
# after all processing on a file is done for the day we must close it
# so as to prevent data currupption