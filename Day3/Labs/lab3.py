import string
#write a custom exception, then an inclusive test, then write the code for the following functions:


class stringException(Exception): # inherits from Exception
  def __init__(self, value):
    Exception.__init__(self, "%s is not text!" %value)
    
class multipleWordException(Exception): # inherits from Exception
  def __init__(self, value):
    Exception.__init__(self, "%s is only one word!" %value)
      

def shout(txt):
	if not isinstance(txt, str):
		raise stringException(txt)
	else:
		return txt.upper() + "!"

## reverses entire string
def reverse(txt):
	return txt[::-1]
	
## reverses just words
def reversewords(txt):
	if " " not in txt:
		raise multipleWordException(txt)
	else:
		words = txt.split()
		return ' '.join(reversed(words))

## reverses letters in each word.
def reversewordletters(txt):
	words = txt.split()
	output = []
	for w in words:
		output.append(reverse(w))
	return ' '.join(output)
		
   
def piglatin(txt):
	words = txt.split()
	vowels = ["a", "e", "i", "o", "u"]
	output = []
	for w in words:
		first_letter = list(w)[0]
 		if first_letter in vowels:
 			w += "a"
 		else:
 			w = (w[1:] + first_letter + "a")
		output.append(w)
	return ' '.join(output)

		
		
		
		
			
			
			
			
			
			

