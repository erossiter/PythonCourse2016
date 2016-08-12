def ordinalFunc(x):
	if not isinstance(x, int):
		return "Input must be integer"
	
	x_string = str(x)
	last_digit = x_string[-1]
	last_2_digits = x_string[-2:]
	
	last_digit = int(last_digit)
	last_2_digits = int(last_2_digits)
	
	if last_2_digits in range(11,16):
		return "%sth" % x
	else:
		if last_digit == 1:
			return "%sst" % x
		if last_digit == 2:
			return "%snd" % x
		if last_digit == 3:
			return "%srd" % x
		if last_digit == 4 or last_digit == 0:
			return "%sth" % x
	
	


## 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th
## 11th, 12th, 13th, 14th, 15th, 16th, 17h, 18th, 19th, 20th
## 21st, 22nd, 23rd, 24th, 25th, 26th