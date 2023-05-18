import random


class PGenerator:
    """construct password in the object
    Args:
        Password len (int)
    Return:
        None
    Rises:
        None (if password lenth < 4)
    """
    def __init__(self, passsize: int) -> None:
        # password lenth should be greater than 3 so that every item(lowercase,upper
        # case, number, puch) can be inserted
        self.__pass_size = passsize
        # store the generated password
        self.password = 'Too Short'
        if self.__pass_size >= 4:
            self.__generator()
	# return random value in the range
    # using a temp variable so that it can handle self argument which will be
    # autometically given by the class. there is no use of this argument
    __uppercaseLetter = lambda temp: chr(random.randint(ord('A'), ord('Z')))
    __lowercaseletter = lambda temp: chr(random.randint(ord('a'), ord('z')))
    __digit = lambda temp: str(random.randint(0, 9))
    __punc_part_1 = lambda temp: chr(
        random.randint(33, 47))  # 15 punct signs (! to /)
    __punc_part_2 = lambda temp: chr(
        random.randint(58, 64))  # 7 punct signs (: to @)
    # 6 punct signs ([ to `)
    __punc_part_3 = lambda temp: chr(random.randint(91, 96))
    # 4 punct signs ({ to ~)
    __punc_part_4 = lambda temp: chr(random.randint(123, 126))
    #
    #

    # private
    def __punctuationSign(self) -> chr:
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
        all_puch_parts = ["punc_part_1","punc_part_2", "punc_part_3", "punc_part_4"]
        randomly_choosed_punch_part = random.choice(all_puch_parts)
        match randomly_choosed_punch_part:
            case "punc_part_1":
                return self.__punc_part_1()
            case "punc_part_2":
                return self.__punc_part_2()
            case "punc_part_3":
                return self.__punc_part_3()
            case default:
                return self.__punc_part_4()

    def __generator(self) -> None:
        """set "pass_size" digit password
        
        this function will return a "pass_size" digit password
        
        Args:
            pass_size (int) : password size
        Return:
            None
        Raises:
            ValueError : if "pass_size" is not a valid integer
        """
        # list of possible password elements
        passElements = ["uppercaseLetter", "lowercaseletter", "digit", "punctuationSign"]
        generated_password = [] # we used list here so that we can suffle the list after this loop (string immutable)
        # generate first 4 base password
        generated_password.append(str(self.__uppercaseLetter()))
        generated_password.append(str(self.__lowercaseletter()))
        generated_password.append(str(self.__digit()))
        generated_password.append(str(self.__punctuationSign()))
        random.shuffle(generated_password)
        self.__pass_size -= 4
        for i in range(self.__pass_size):
            # choicing a random element for the password and appending to password
            element = random.choice(passElements)
            match element:
                case "uppercaseLetter":
                    generated_password.append(str(self.__uppercaseLetter()))
                case "lowercaseletter":
                    generated_password.append(str(self.__lowercaseletter()))
                case "digit":
                    generated_password.append(str(self.__digit()))
                case default:
                    generated_password.append(str(self.__punctuationSign()))
        random.shuffle(generated_password) # shuffling the password
        self.password =  "".join(generated_password) # set password

class SetDependencies:
    """
    setup all dependencies for running the program
    """
    # check if the file present or not
    def setFiles(self):
        # creating admin.txt and saved_passwords.txt file if not present 
        f = open('admin.txt', 'a')
        f.close()
        f = open('saved_passwords.txt', 'a')
        f.close()
