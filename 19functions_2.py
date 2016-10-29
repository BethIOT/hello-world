def cookies_nuts (cookie_count, box_nuts) :
	print "You have %d cookies" %cookie_count
	print 'You have %d box of nuts' %box_nuts
	print 'Now put nuts in your cookies'
	tot = cookie_count*box_nuts
	print "Bake em and get %d nutty cookies \n" %tot

print "We can feed data directly : "
cookies_nuts(20,30)

print "OR we could use variables : "
cookies = 50
nuts = 20
cookies_nuts (cookies, nuts)

print "You could also do math in parameter : "
cookies_nuts (15+12, 2*8)

print "You could also do math on variables : "
cookies_nuts (cookies/2, nuts*53)