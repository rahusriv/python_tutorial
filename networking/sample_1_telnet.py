import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
#password = input("Enter your telnet password: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"ls\n")
#tn.write(b"enable\n")
#tn.write(b"enablepwd\n")
#tn.write(b"conf t\n")
#tn.write(b"int loop 0\n")
#tn.write(b"ip address 10.33.44.55 255.255.255.0\n")
#tn.write(b"end\n")
tn.write(b"exit\n")

#print(tn.read_all().decode('ascii'))