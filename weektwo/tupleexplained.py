# # declaring tuple as a literal
# lisofnames=('christian',12)



# # declaring list
# listoforanges=[1,"string",11]



# print(listoforanges)

# thedictionaries={"one":1,"two":2,"firstletter":"c"}
# print(thedictionaries.get('one'))
import time
# Write a program that calculate the cgp of three courses
courses=['chemistry','biology','crk']
grade=""
i=0
listofgrade=[]
# grade={'gradeone':'A','gradetwo':'B','gradethree':'C','gradefour':'D','gradefour':'F'}
while(i<=2):
   thescore= input("What is your score in "+str(courses[i])+"\n ")
   i=i+1
   if int(thescore)>=70 and int(thescore)<=100:
      grade="A"  
      listofgrade.insert(0,grade)
   elif int(thescore)>=60 and int(thescore)<70:
      grade="B"
      listofgrade.insert(1,grade)
   elif int(thescore)>=50 and int(thescore)<60:
      grade="C" 
      listofgrade.insert(2,grade)
for j in range(3):
   print("Your grade in "+str(courses[j])+" is \t"+str(listofgrade[j])+"\n")