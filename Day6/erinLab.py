#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def gcd(x, y, org_min = None):
	if org_min == None:
		org_min = min(x,y)
	if x == 0 or y == 0:
		return None
	if (y % x == 0) and (org_min % x == 0):
		return x
	return gcd(min(x, y) - 1, max(x, y), org_min)

#print gcd(4, 8)
#print gcd(7, 12)
#print gcd(8, 12)
#print gcd(16, 14)


#Exercise 2
#Write a function that returns prime numbers less than 121

def p(num, primes = []):
	if num == 2:
		primes.append(2)
		return primes
	else:
		i = num - 1
		while i > 1:
			if num % i == 0:
				break #not a prime
			i -= 1
		else:
			primes.append(num)
	return p(num - 1)

#print p(num = 121)


