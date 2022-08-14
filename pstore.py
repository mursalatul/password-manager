
class PStore:
    def pStoreInTxt(salf, password):
        f = open("saved_passwords.txt", "at")
        f.write(password + "\n")
        f.close()
