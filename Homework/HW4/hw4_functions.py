## Exception to catch when an empty list
## is passed to either sort function
class emptyListException(Exception):
  def __init__(self):
    Exception.__init__(self, "List must be non-empty.")


## complexity worst case: O(n^2)
def insertion_sort(x):
	if len(x) == 0:
		raise emptyListException()
	for i in range(1, len(x)):
		val = x[i]
		pos = i
		while x[pos-1] > val and pos > 0:
			x[pos], x[pos-1] = x[pos-1], x[pos]
			pos -= 1
	return x

## complexity worst case: O(n log n)
def combine(x1, x2):
	## 1 element lists
	if len(x1) == 1 and len(x2) == 1:
		if x1 < x2:
			out = x1 + x2
		else:
			out = x2 + x1
	## when lists can simply be concatenated
	if x2[-1] < x1[0]:
		out = x2 + x1
	elif x1[-1] < x2[0]:
		out = x1 + x2
	## when elements need to be merged
	else:
		out = x1
		for i in range(0, len(x2)):
			inc_index = 0
			for j in range(0, len(x1)):
				if x2[i] > x1[j]:
					continue
				else:
					out.insert(j + inc_index, x2[i])
					inc_index += 1
					break
			else:
				out.append(x2[i])
	return out

def merge_sort(x):
	if len(x) == 0:
		raise emptyListException()
	if len(x) == 1:
		return x
	else:
		mid = len(x)/2
		x1 = merge_sort(x[mid: ])
		x2 = merge_sort(x[ :mid])
		return combine(x1, x2)
