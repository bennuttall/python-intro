sum = 0
for n in xrange(1,1000):
    if n % 3 == 0 or n % 5 == 0: sum += n
print sum