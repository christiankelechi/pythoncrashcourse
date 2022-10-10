# A prgramme that permits only users in Nigeria to access bank dashboard
for numoftimes in range(10):
    
    name=input("What is your Name?\n")
    country=input('Type in your Country\n')

    if country.lower()=="Nigeria".lower():
        print("Welcome to Access Bank Dash board\n")

    else:
        print("You cant access This Bank\n")
        