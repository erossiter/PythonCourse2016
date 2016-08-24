
## complexity: O(n^2)
def insertion_sort(x):
	for i in range(1, len(x)):
		val = x[i]
		pos = i
		while x[pos-1] > val and pos > 0:
			x[pos], x[pos-1] = x[pos-1], x[pos]
			pos -= 1
	return x

a = [4, 3, 2, 1, 10, 2, 12 ]
b = [1]
c = range(100)
random.shuffle(c)

insertion_sort(a)
insertion_sort(b)
insertion_sort(c)


def combine(x1, x2):
	if len(x1) == 1 and len(x2) == 1:
		if x1 < x2:
			out = x1 + x2
		else:
			out = x2 + x1
	else:
		## if the last element of the bigger list
		## is smaller than the first element of the
		## smaller list, then put it first
		if x2[-1] < x1[0]:
			out = x2 + x1
		if x2[0] > x1[-1]:
			out = x1 + x2
		#if x2[0] > x1[0] and x2[-1] < x1[-1]: 
	return out



def merge_sort(x):
	if len(x) == 1:
		return x
	else:
		mid = len(x)/2
		x1 = x[mid: ]
		x2 = x[ :mid]
		x1 = merge_sort(x1)
		x2 = merge_sort(x2)
		return combine(x1, x2)
	#print ms_x1
	#print ms_x2
	#combine(ms_x1, ms_x2)


	#	return merge_sort(x2)
		#return combine(x1, x2)
	
	#mid = len(x)/2
	#x1 = x[ :mid]
	#x2 = x[mid: ]
	#return merge_sort(x1, x2)
	#return merge_sort(x2)























