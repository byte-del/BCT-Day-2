l=[]
def signup():
    email=input("Enter email id: ")
    password=input("Enter password: ")
    a={"email": email ,"password": password}
    l.append(a)
    print(l)
signup()
