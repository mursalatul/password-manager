from cryptography.fernet import Fernet

# encryption
# 
# 
def key_combination(generated_encrypt_key):
    """
    Combine fernet generated key and admin password.
    
    Args:
        Key (str): Fernet generated key.
    Return:
        None.
    """
    admin_password = None

    # retriving admin password
    with open('admin.txt', 'r') as f:
        f.readline() # first line is the admin username
        admin_password = f.readline()[:-1] # second line is the password. removing the ending \n with [:-1]
    
    # pusing adming passworing into Fernet generated key. last character should be '=' sign.
    admin_password = generated_encrypt_key[:- len(admin_password) - 1] + admin_password.encode() + b'='
    
    return admin_password

# creating universal encrypt key from admin password
FERNET_GENERATED_ENCRYPT_KEY = Fernet.generate_key()
MY_ENCRYPT_KEY = key_combination(FERNET_GENERATED_ENCRYPT_KEY)

# 
# 
# 
class PStore:
    # store username and password
    def pStore(self, uname: str, pword: str)->None:
        """
        Store PStore object(username and password)
        """
        self.__username = uname
        self.__password = pword
        
        # encrypt the username and password first
        # self.encrypt()
        print(MY_ENCRYPT_KEY)
        f = open('saved_passwords.txt', 'at') # opening file
        
        # writing the data
        f.write(self.__username + '\n')
        f.write(self.__password + '\n')
        f.close()
    
    def pshow(self, uname: str)->str:
        """
        Show password for the particular username
        """
        __provided_username = uname
        saved_password = None
        
        f = open('saved_passwords.txt', 'rt') # opening file in read mode
        
        user = f.readline()
        while user:
            # user = self.decrypt(user)
            user = user[:-1] # [:-1] = removing ending \n
            if user == __provided_username:
                saved_password = f.readline()[:-1] # [:-1] = removing ending \n
                break
            user = f.readline()
        f.close()
        
        if saved_password == None:
            return "Username Not Found!"
        else:
            return saved_password
        
    def __encrypt(self):
        pass
