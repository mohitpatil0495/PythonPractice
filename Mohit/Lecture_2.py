str1 = "Mohit"
str2 = "Patil"
m = 23
pin = len(str1)

str_3 = str1 +" " + str2

print("\t", str_3)

print(len(str1))
print (pin)
print(len(str2)) 

 name = "mohit patil"

print(name[-1:-8])
print(name[0:len(name)]) 


 str = "hey i am mohit patil. I'm learning python from apna college."

print(str.endswith("ge."))
print(str.capitalize())
print(str.replace("i", "o"))
print(str.find("from"))
print(str.count("i"))
print(str.count("I")) 


#PQ WAP to input user’s first name & print its length
name = input("Enter your full name: ")

print(name)
print(len(name))

#WAP to find the occurrence of ‘$’ in a String.
salary = "Mohit Patil's salary is $80000"

print(salary.find(count("$"))) 

""" #conditional statement 
age = int(input("enter your age"))

if (age >= 18):
    print("You can drive")
else:
    print("You cannot drive") """


marks = int(input("enter your marks: "))

    if (marks >= 90):
       grade = "A"
    elif(90 > marks >= 80): # you can also combine the condtion"90 > marks and marks >= 80"
       grade = "B"
    elif(80 > marks >= 70):
     grade = "C"
     else:
      grade = "D"


# print("Your grade is: ",grade)    