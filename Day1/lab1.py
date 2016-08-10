## (1)
def binarify(num):
	"""convert positive integer to base 2"""
	if num <= 0:
		return '0'
		
	digits = []
	while num > 0:
		digits.append(num % 2)
		num = num / 2

	#assigns digits the sequence from the first to the last
	#element in digits, starting with the last one.
	digits = digits[::-1] 
	
	#.join() concatenates
	return ''.join(str(i) for i in digits)
  

## (2)
def int_to_base(num, base):
	"""convert positive integer to a string in any base"""
	if num <= 0 or base <= 0:
		return '0'
	if base == 1:
		return num
	
	neg = False
	if num < 0:
		num *= -1
		neg = True
		
	digits = []
	while num > 0:
		digits.append(num % base)
		num = num / base
	digits = digits[::-1]
	
	if neg:
		return '-'+''.join(str(i) for i in digits)
	
	return ''.join(str(i) for i in digits)
	


## (3) 
def base_to_int(string, base):
	if string == "0" or base <= 0:
		return 0
	
	neg = False
	if string[0] == '-':
		string = string[1: ]
		neg = True
	
	result = 0
	num = len(string)
	for i in string:
		num -= 1
		result += ((base ** num) * int(i))
	if neg:
		return result * (-1)
	
	return result


## (4)
def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  return base_to_int(str1, base1) + base_to_int(str2, base2)

## (5)
def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  return base_to_int(str1, base1) * base_to_int(str2, base2)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  if(num < 0 or num > 3999):
  	return "invalid entry"
  
  ans = ""
  
  while num >= 1000:
  	ans += "M"
  	num -= 1000

  while num >= 900:
  	ans += "CM"
  	num -= 900

  while num >= 500:
  	ans += "D"
  	num -= 500

  while num >= 400:
  	ans += "CD"
  	num -= 400
  	
  while num >= 100:
  	ans += "C"
  	num -= 100
  
  while num >= 90:
  	ans += "XC"
  	num -= 90
  
  while num >= 50:
  	ans += "L"
  	num -= 50
  
  while num >= 40:
  	ans += "XL"
  	num -= 40
  
  while num >= 10:
  	ans += "X"
  	num -= 10
  
  while num >= 9:
  	ans += "IX"
  	num -= 9
  
  while num >= 5:
  	ans += "V"
  	num -= 5
  
  while num >= 4:
  	ans += "IV"
  	num -= 4
  
  while num >= 1:
  	ans += "I"
  	num =- 1

  return ans



## Checking all functions
print binarify(16) 
print binarify(0)
print binarify(123)
print int_to_base(123, 2)
print base_to_int("10000", 2)
print romanify(3999)


# # Copyright (c) 2014 Matt Dickenson
# # 
# # Permission is hereby granted, free of charge, to any person obtaining a copy
# # of this software and associated documentation files (the "Software"), to deal
# # in the Software without restriction, including without limitation the rights
# # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the Software is
# # furnished to do so, subject to the following conditions:
# # 
# # The above copyright notice and this permission notice shall be included in all
# # copies or substantial portions of the Software.
# # 
# # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# # SOFTWARE.