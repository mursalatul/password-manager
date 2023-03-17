class PStore:
    username , password = 0, 0
    # store username and password
    def pStore(self, uname: str, pword: str)->None:
        """
        Store PStore object(username and password)
        """
        self.username = uname
        self.password = pword
        # encrypt the username and password first
        # self.encrypt()
        f = open('saved_passwords.txt', 'at') # opening file
        f.write(self.username + '\n' + self.password + '\n') # writing the data
        f.close()
    
    def pshow(self, uname: str)->str:
        """
        Show password for the particular username
        """
        self.username = uname
        saved_password = None
        f = open('saved_passwords.txt', 'rt') # opening file in read mode
        user = f.readline()
        while user:
            # user = self.decrypt(user)
            user = user[:-1] # [:-1] = removing ending \n
            if user == self.username:
                saved_password = f.readline()[:-1] # [:-1] = removing ending \n
                break
            user = f.readline()
        f.close()
        if saved_password == None:
            return "Username Not Found!"
        else:
            return saved_password