def greet_user(name):
    print(f"Hello, {name}! Welcome to the exploring-uv project.")

def main():
    print("Running main.py...")
    name = input("What's your name? ")
    greet_user(name)

if __name__ == "__main__":
    main()