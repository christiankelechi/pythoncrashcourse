from Student import Profile

pr=Profile("Kc","299","Male",1)
pr.name=input("Enter your name\n")
pr.regnumber=input("What is your Regnumber\n")
gender=input("What is your gender\n")
pr.age=int(input("What is your age"))
print('Your name is '+pr.name+" your regnumber is "+pr.regnumber+" and your gender is "+pr.gender+str(pr.age))



