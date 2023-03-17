import pgenerator, pstore

def main():
    pass_object = pgenerator.PGenerator()
    p = int(input("How many password you want to generate: "))
    for _ in range(p):
        size = int(input("Password size = "))
        password = pass_object.generator(size)
        print("Pass :", password)
        save_pass_query = input("Do you want to save it? (Yes / No)").strip().lower()
        pass_store = pstore.PStore()
        if save_pass_query in ["yes", "y", 1]:
            username = input("Username: ")
            # saving password in store
            pass_store.pStore(username, password)
        search_pass_query = input("Search password(yes/no): ").strip().lower()
        if search_pass_query in ["yes", 'y', 1]:
            username = input("Username: ")
            # search for the user name
            print(pass_store.pshow(username))

if __name__ == "__main__":
	main()