class Login(object):

    def __init__(self,name,password):
        self.name = name
        self.password = password

    def login(self):
        self.name = "rahul"#print("Please enter you username:")
        self.password = "rahul12"#print("Please enter your password:")
        password_file_name = str(self.name)+str("_password.txt")
        print(password_file_name)
        f = open(password_file_name,"r")
        pwd = f.read()
        #pwd.strip(" ")
        pwd.rstrip()
        print(repr(pwd))
        #pwd.strip(" ")
        #print(self.password)
        if self.password == pwd:
            print("You have successfully logged in.")
        else:
            print("Sorry , wrong credentials")


if __name__ == "__main__":
    a = Login("rahul","rahul12")

    a.login()
    print(a.__dict__)