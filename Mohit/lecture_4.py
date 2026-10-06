#dictionary in python 
""" student = {
    "name": "mohit",
    "subjects" : {      # nested dictionary
        "math" : 98,
        "chem" : 87,
        "phy" : 86,
    }

} """

""" student["name"] = "rani"
print(student)
print(student["subjects"]["chem"])
print(student)
print(list(student.keys()))
print(student.values())
print(student.items())
print(student.get("name"))
student.update({"age": 21})
student.update({"name": "chandal"})

print(student)"""

#sets
""" collection = {1, 2, 4, 3}
classy = {5, 8, 2, 6, 7 } """
""" print(type(collection))
print(type(classy)) """
""" collection.add(5)
collection.remove(3)
collection.pop()
print(collection) """
""" print(collection.union(classy))
print(collection.intersection(classy))
print(collection)
collection.clear()
print(collection) """

#Practice questions
""" dict = {
    "table" : ("a peice of furniture", "list of figure & fact"),
    "cat" : "a small animal"
}
print(dict) """

""" student = {
    "python", "java", "c++", "python", "javascript", 
     "java", "python", "java", "c++", "c"
    }

print(len(student)) """
""" 
marks = {}

phy = int(input("physics marsk: "))
marks.update({"phy " : phy})

math = int(input("math marks: "))
marks.update({"math " : math})

chem = int(input("chemistry marks: "))
marks.update({"chem" : chem})

print(marks) """
""" 
values = {
    ("float" , "9.0"),
    ("int" , "9"),
}

print(values) """

""" list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for mohit in list:
    print(mohit) """

""" tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 81
idx = 0
# print(tup.index(x))
for m in tup:
    if (x == m):
        print ("x is found ", idx)
        break
    idx += 1
    print(m) """

""" for i in range(101, 0, -1):
    print(i)
else: 
    print("end") """
a = int(input("enter a number: "))
b= a * 11
for i in range(a, b, a):
    print(i)
else:
    print("end")
