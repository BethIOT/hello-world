from sys import argv

# 'import' adds functions to python
# we use this to bring a module(small lib) of codes into our prgm
# argv = argument variable
# argv is a sys fn("from sys"). it is contains (actually it passes)
# the variables we send to the system funtion.
# in our case, eveything following ./python are the variables

script, var1, var2, var3, var4 = argv

print "The script called is : ", script
print "The first variable is : ", var1
print "The second variable is : ", var2
print "The third variable is : ", var3
print "The fourth variable is : ", var4


# in cmd line, we must type in 3 more variables following the file_name
# Eg : >.\python lesson13.py bricks make walls strong
# script=lesson13.py ; var1=bricks ; var2=make ; var3=walls ; var4=strong
# argv must contain exact no of variables. no more. no less
