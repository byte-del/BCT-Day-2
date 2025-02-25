l = []
def signup():
    email = input("Enter email id: ")
    password = input("Enter password: ")
    a = {"email": email, "password": password}
    l.append(a)
    print("Signup successful")
def signin():
    email = input("Enter email id: ")
    password = input("Enter password: ")
    
    for user in l:
        if user["email"] == email and user["password"] == password:
            print("Signin successful")
            return
    print("Invalid credentials")
while True:
    print("\n1. Signup\n2. Signin\n3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        signup()
    elif choice == "2":
        signin()
    elif choice == "3":
        print("Exiting")
        break
    else:
        print("Invalid choice, try again.")
