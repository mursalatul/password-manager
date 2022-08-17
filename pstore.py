
class PStore:
    # store passwords in a particular file
    def pStoreInTxt(salf, password):
        f = open("saved_passwords.txt", "at")
        f.write(password + "\n")
        f.close()
