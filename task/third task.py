import getpass
import codecs
import sys

userid = {}  # create a dictionary to store the user information

# pass_file=sys.argv[1]
pass_file = "passwd.txt"


def adduser():
    # to add new user create their profilio and create their username
    with open(pass_file, 'r') as file:
        make_good = file.readlines()

    username = input("Enter name: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter your password: ")
    password = codecs.encode(password, "rot13")


    for i in make_good:
        name = i.strip().split(':')[0]
        if username == name:
            print("sorry this username is already taken please choose another unique username\n")
            adduser()

    make_good.append(f"{username}:{real_name}:{password}\n")


    with open(pass_file, "w") as file:
        file.writelines(make_good)

def log_in():
    # to log into the user file
    with open(pass_file, 'r') as file:
        make_good = file.readlines()

    username = input("Enter name: ")
    password = getpass.getpass("Enter your password: ")
    password = codecs.encode(password, "rot13")

    for i in make_good:
        name = i.strip().split(':')[0]
        passwd = i.strip().split(':')[2]

        found = False

        if username == name:
            if password == passwd:
                found = True
                print ("you have logged in successfully")
            
    if not found:
        print("Not found")


def del_user():
    # to delete the existing user
    with open(pass_file, 'r') as file:
        make_good = file.readlines()

    username = input("Enter name: ")
    password = getpass.getpass("Enter your password: ")#cant see me
    password = codecs.encode(password, "rot13")#cant read me

    for j,i in enumerate(make_good):
        name = i.strip().split(':')[0]

        found = False

        if username == name:
            del make_good[j]

    if not found:
        print("Not found")

    with open(pass_file, "w") as file:
        file.writelines(make_good)
        

print("register your sampati here now")
adduser()
print ("log in now bitch the same thing you have here")
log_in()
print("Delr")
del_user()
