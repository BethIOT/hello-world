# Tried getting data from user for the 3 functions below, but it crashes
# fixed this issue by feeding type to raw input
i=0
num1=[]
while i<6:
	print "At the top i is %d"%i
	num1.append(i)
	i+=1
	print "The list is : ", num1
	print "At the bottom i is %d" %i
print "So the number list is"
for n in num1:
	print n

print
def trial_1(lt):
	i=0
	num2=[]
	while i<lt:
		print "Item is %d"%i
		num2.append(i)
		i+=1
	print num2
print "Limit of list is "
lt = int(raw_input('?? '))
trial_1(lt)

print
def trial_2(lt, st):
	i=0
	num3=[]
	while i<lt:
		print "Item is %d"%i
		num3.append(i)
		i+=st
	print num3
print "Limit and step of list are "
lt = int(raw_input('?? '))
sz = int(raw_input('?? '))
trial_2(lt,sz)

print
def trial_3(lt, st):
	num4=range(0,lt,st)
	for i in num4:
		print "Item is %d"%i
	print num4
print "Using for loop here; Limit and step of list are "
lt = int(raw_input('?? '))
sz = int(raw_input('?? '))
trial_3(lt,sz)
