#Python program of a simple calculator  which performs basic arithmetic operations using functions

def add(a,b):
    return(a+b)

def subtract(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def division(a,b):
    return(a/b)

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))

print("please select the operation")
print("a. add")
print("b. subtract")
print("c. multiply")
print("d. division")


choice=input("enter the choice from (a/b/c/d): ")


if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice=='d':
    print(num1,"/",num2,"=",division(num1,num2))

else:
    print("this is an invalid input")    

      

