import random

# return random value in the range
uppercaseLetter = lambda : chr(random.randint(ord('A'), ord('Z')))
lowercaseletter = lambda : chr(random.randint(ord('a'), ord('z')))
digit = lambda : str(random.randint(0, 9))
punctuationSign = lambda : chr(random.randint(33, 47))

def generator(passSize):
	"""return "passSize" digit password

	this function will return a "passSize" digit password

	Args:
		passSize (int) : password size
	Return:
		The str version of the password
	Raises:
		ValueError : if "passSize" is not a valid integer
	"""
	# list of possible password elements
	passElements = ["uppercaseLetter", "lowercaseletter", "digit", "punctuationSign"]
	password = []
	for i in range(passSize):
		# choicing a random element for the password and appending to password
		element = random.choice(passElements)
		match element:
			case "uppercaseLetter":
				password.append(uppercaseLetter())
			case "lowercaseletter":
				password.append(lowercaseletter())
			case "digit":
				password.append(digit())
			case default:
				password.append(punctuationSign())
	random.shuffle(password) # shuffling the password
	return "".join(password) # returning as a string

p = int(input("How many password you want to generate: "))
for _ in range(p):
	size = int(input("Password size = "))
	print("Pass :", generator(size))
