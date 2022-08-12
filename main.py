import pgenerator

def main():
    pass_object = pgenerator.PGenerator()
    p = int(input("How many password you want to generate: "))
    for _ in range(p):
        size = int(input("Password size = "))
        print("Pass :", pass_object.generator(size))

if __name__ == "__main__":
	main()