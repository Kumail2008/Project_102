
print("Pick the two numbers you want to add, subtract, multiply, or divide")
a = int(input("First value: "))
b = int(input("Second value: "))
operation = input("Please enter operation (Multiply, Subtract, Add, Divide)")




def add():
    c = a + b
    print ("Answer is....")
    print(c)

def subtract():
    c = a-b
    print ("Answer is....")
    print(c)    

def divide():
    c = a/b
    print ("Answer is....")
    print(c)  

def multiply():
    c = a*b
    print ("Answer is....")
    print(c)      
  

if operation == 'Add':
    add()

elif operation == 'Divide':
    divide() 

elif operation == 'Subtract':
    subtract()

else:
    multiply()  