"""
Helper function to detect whether there are more than 2 identical characters in sequence in the given string
@ input  : string need to be checked
@ output : the indices of the sequenctial characters in the form [(start_1, end_1), ..., (start_m, end_m)]
"""
def consecutive(string):
	import re
	result = list(re.finditer(r'(.)\1\1+', string))
	return [(m.start(), m.end()) for m in result]

"""
Finite State Transducer for the Soundex algorithm
"""
#lists of conversions
v  = set(['a','e','h','i','o','u','w','y'])
q1 = set(['b','f','p','v'])
q2 = set(['c','g','j','k','q','s','x','z'])
q3 = set(['d','t'])
q4 = set(['l'])
q5 = set(['m','n'])
q6 = set(['r'])

def removeNonInitial(string):
	newString = string[0]
	for letter in string[1:]:
		if letter.lower() not in v:
			newString += letter
	return newString

def encode(string):
	newString = string[0]
	for letter in string[1:]:
		if letter.lower() in q1:
			newString += '1'
		elif letter.lower() in q2:
			newString += '2'
		elif letter.lower() in q3:
			newString += '3'
		elif letter.lower() in q4:
			newString += '4'
		elif letter.lower() in q5:
			newString += '5'
		elif letter.lower() in q6:
			newString += '6'
		else:
			import sys
			sys.exit("--- There shouldn't be any letter within ['a','e','h','i','o','u','w','y'] ---")
	return newString

def cleanSequence(String):
	newString = string[0]
	# TBI
	return newString

def truncateOrPadding(String):
	newString = string[0]
	# TBI
	return newString

def soundex(name):
	# TBI
	pass

def test():
	assert removeNonInitial("Maehisss") == "Msss"
	assert removeNonInitial("AaEhi") == "A"
	assert encode("Msss") == "M222"
	print "---Pass---"

test()