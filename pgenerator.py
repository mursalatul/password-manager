import random

# return random value in the range
uppercaseLetter = lambda : chr(random.randint(ord('A'), ord('Z')))
lowercaseletter = lambda : chr(random.randint(ord('a'), ord('z')))
digit = lambda : str(random.randint(0, 9))
punc_part_1 = lambda : chr(random.randint(33, 47)) # 15 punct signs (! to /)
punc_part_2 = lambda : chr(random.randint(58, 64)) # 7 punct signs (: to @)
punc_part_3 = lambda : chr(random.randint(91, 96)) # 6 punct signs ([ to `)
punc_part_4 = lambda : chr(random.randint(123, 126)) # 4 punct signs ({ to ~)

def punctuationSign():
	"""return random punctuation sign from 32 signs of ASCII table

	this function will randomly choose one punctuation sign from 32
	indivitual signs.
	Args:
		None
	Return:
		1 Sign
	Raises:
		None
	"""
	all_punctuations = ["punc_part_1", "punc_part_2", "punc_part_3", "punc_part_4"]
	punch = random.choice(all_punctuations)
	match punch:
		case "punc_part_1":
			return punc_part_1()
		case "punc_part_2":
			return punc_part_2()
		case "punc_part_3":
			return punc_part_3()
		case default:
			return punc_part_4()

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
	password = [] # we used list here so that we can suffle the list after this loop (string immutable)
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
