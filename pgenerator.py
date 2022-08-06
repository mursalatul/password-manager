import random

def generator() -> str:
	"""return 6 digit password

	this function will return a 6 digit password where first
	of the 2 letters are capital, second 2 letters are lower,
	3rd 2 parts are digits and last 2 parts are punctuations

	Args:
		None
	Return:
		The str version of the password
	Raises:
		None
	"""
	uppercaseLetter1 = chr(random.randint(ord('A'), ord('Z')))
	uppercaseLetter2 = chr(random.randint(ord('A'), ord('Z')))
	lowercaseletter1 = chr(random.randint(ord('a'), ord('z')))
	lowercaseletter2 = chr(random.randint(ord('a'), ord('z')))
	digit1 = chr(random.randint(ord('0'), ord('9')))
	digit2 = chr(random.randint(ord('0'), ord('9')))
	punctuationSign1 = chr(random.randint(33, 47))
	punctuationSign2 = chr(random.randint(33, 47))
	password = uppercaseLetter1 + uppercaseLetter2 + lowercaseletter1 + lowercaseletter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
	password = list(password)
	random.shuffle(password)
	password = "".join(password)
	return password

print("password =", generator())