
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
	if x2[-1] < x1[0]:
		out = x2 + x1
	elif x1[-1] < x2[0]:
		out = x1 + x2
	else:
		for i in range(0, len(x2)):
			for j in range(0, len(x1)):
				if x2[i] > x1[j]:
					continue
				else:
					x1.insert(j, x2[i])
		out = x1
	return out
	

[4,6,8]  [5,7,9]


def merge_sort(x):
	if len(x) == 1:
		return x
	else:
		mid = len(x)/2
		x1 = merge_sort(x[mid: ])
		x2 = merge_sort(x[ :mid])
		return combine(x1, x2)























