users = {'Ahmed': '1394',
        'Ali': '6078',
        'Amr': '9345'}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Welcome, {}!" .format(username))
    else:
        print("Incorrect Entry.")

login()
