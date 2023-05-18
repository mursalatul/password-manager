class PStore:
    # store username and password
    def pStore(self, uname: str, pword: str)->None:
        """
        Store PStore object(username and password)
        """
        self.__username = uname
        self.__password = pword
        
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
        
