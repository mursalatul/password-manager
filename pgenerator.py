import random


class PGenerator:
    
	# return random value in the range
    # using a temp variable so that it can handle self argument which will be
    # autometically given by the class. there is no use of this argument
    uppercaseLetter = lambda temp: chr(random.randint(ord('A'), ord('Z')))
    lowercaseletter = lambda temp: chr(random.randint(ord('a'), ord('z')))
    digit = lambda temp: str(random.randint(0, 9))
    punc_part_1 = lambda temp: chr(
        random.randint(33, 47))  # 15 punct signs (! to /)
    punc_part_2 = lambda temp: chr(
        random.randint(58, 64))  # 7 punct signs (: to @)
    # 6 punct signs ([ to `)
    punc_part_3 = lambda temp: chr(random.randint(91, 96))
    # 4 punct signs ({ to ~)
    punc_part_4 = lambda temp: chr(random.randint(123, 126))
    #
    #
    
    def punctuationSign(self):
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
        # selecting one of four punctuation parts set
        # calling lambda function of the choosed punch part's 
        self.all_puch_parts = ["punc_part_1","punc_part_2", "punc_part_3", "punc_part_4"]
        self.randomly_choosed_punch_part = random.choice(self.all_puch_parts)
        match self.randomly_choosed_punch_part:
            case "punc_part_1":
                return self.punc_part_1()
            case "punc_part_2":
                return self.punc_part_2()
            case "punc_part_3":
                return self.punc_part_3()
            case default:
                return self.punc_part_4()

    def generator(self, pass_size):
        """return "pass_size" digit password
        
        this function will return a "pass_size" digit password
        
        Args:
            pass_size (int) : password size
        Return:
            The str version of the password
        Raises:
            ValueError : if "pass_size" is not a valid integer
        """
        # list of possible password elements
        self.passElements = ["uppercaseLetter", "lowercaseletter", "digit", "punctuationSign"]
        self.password = [] # we used list here so that we can suffle the list after this loop (string immutable)
        for i in range(pass_size):
            # choicing a random element for the password and appending to password
            self.element = random.choice(self.passElements)
            match self.element:
                case "uppercaseLetter":
                    self.password.append(str(self.uppercaseLetter()))
                case "lowercaseletter":
                    self.password.append(str(self.lowercaseletter()))
                case "digit":
                    self.password.append(str(self.digit()))
                case default:
                    self.password.append(str(self.punctuationSign()))
        random.shuffle(self.password) # shuffling the password
        return "".join(self.password) # returning as a string
