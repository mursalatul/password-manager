import pgenerator, pstore

def main():
    pass_object = pgenerator.PGenerator()
    pass_store_object = pstore.PStore()
    p = int(input("How many password you want to generate: "))
    for _ in range(p):
        size = int(input("Password size = "))
        password = pass_object.generator(size)
        print("Pass :", password)
        save_pass_query = input("Do you want to save it? (Yes / No)").strip().lower()
        if save_pass_query in ["yes", "y", 1]:
            pass_store_object.pStoreInTxt(password)

if __name__ == "__main__":
	main()