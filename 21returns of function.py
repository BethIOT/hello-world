def add(a, b) :
	print "Adding %d + %d" %(a,b)
	return a+b
def sub(a, b) :
	print "Subtracting %d - %d" %(a,b)
	return a-b
def mult(a, b) :
	print "Multyplying %d * %d" %(a,b)
	return a*b
def div(a, b) :
	print "Dividing %d / %d" %(a,b)
	return a/b
def function(key,di,mu,ad,su):
	print "We will cascade all operations with the key"
	p=div(di,key)
	q=mult(mu,key)
	r=sub(su,key)
	s=add(ad,key)
	return p,q,r,s

print "Lets do math with functions" # this will be first out on console

a1 = add(26,56)
a3 = mult(15,65)
print "sum is %d and product is %d"%(a1, a3)

print "Difference is", sub(99,65)
print "Quotient is", div(88,4)
a2 = sub(99,65)
a4 = div(88,4)

print "Heres a puzzle"
w = add(a1,mult(a3,sub(a2,div(a4,2))))
print "Answer is ", w,"try this problem manually"

print "Heres another function"
r1, r2, r3, r4=function(50,80,90,59,28)
print "These are returned %d %d %d %d together" %(r1,r2,r3,r4)

# for some reason the function in ln_41 is called before prgm starts to print
print "We can also get returns like this %r %r %r %r"%function(52,82,92,52,22)