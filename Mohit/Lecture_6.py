#Function defination
# def model(a, b, c): #parameters
#     sum = a + b + c
#     print(sum)
#     return sum

# model(1, 2, 3) #function call #arguments 

# def model(a=1, b=1): #by default value if user not value pass then they automatically get the default value
#     return a + b
# sum = model(1, 2)
# print(sum)

# def hello():
#     print("Hello Motherfucker")

# hello()
#default parameters
# def calc_sum(a=2, b=2):
#     sum = a * b
#     print(sum)
#     return sum

# calc_sum()

# calc_sum(5, 5)
    
#practice

# ix_class= ["aman", "samarth", "sidhhi"]
# x_class = ["mohit", "vaishnavi", "rashi", "tanu"]

# def mohit_len(list):
#     print(len(list))

# mohit_len(ix_class)
# mohit_len(x_class)

# print("mohit", end=" ")
# print("patil")
 

# def calc_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
        
#     print(fact)

    
# calc_fact(5)

def checker():
    a= int(input("enter a number"))

    if (a % 2 == 0):
        print("Even")
    else:
        print("ODD")
    
    
checker()