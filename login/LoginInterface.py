class Login(object):

    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.login = 0
        self.data = ""

    def user_login(self):
        password_file_name = str(self.name)+str("_password.txt")
        try:
            f = open(password_file_name,"r")
        except:
            print("Wrong login credentials")
            return
        pwd = f.read()
        pwd = pwd.rstrip()
        if self.password == pwd:
            print("You have successfully logged in.")
            self.login =1
        else:
            print("Sorry , wrong credentials")

    def read_my_data(self):
        if(self.login==1):
            self.data = open(self.name+"_data.txt", "r").read()
            print(self.data)
        else:
            print("Sorry , not an authorized used")

    #def send_email()
    #def new_user()


if __name__ == "__main__":
    u = input("Please enter your user name :")
    p = input("Please entr your password: ")
    user1 = Login(u,p)
    user1.user_login()
    user1.read_my_data()
    print(user1.__dict__)