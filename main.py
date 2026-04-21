print("Hello world");
name = 'Shivani'
age =  22
Gender = 'Female'
isStudent = True
print("The name of the student is "+ name + " , her age is " + str(age)+ " and the student of our college  which is - " + str(isStudent));
num = 45
print(num)
num+= 10
print(num)
Food = input(" what is your favourite food \n")
print("Wow ! I also personally like that food : " + Food)
a = int(input( "Enter the value of a \n "))
b = int(input( "Enter the value of b \n "))
print (" a + b:", a + b);
print (" a - b:", a - b);
print (" a / b:", a / b);
print (" a % b: ", a % b);
print (" a //  b: ", a // b)
a = int(input( "Enter the value of a \n "))
print ("the square of a is : ", a**2 );
print ("the square of a is : ", a*a );
print ("the cube of a is : ", a**3 );
print ("the cube of a is : ", a*a*a );
A = int(input("Enter your age : "))
match A :
    case 3 :
        print(" You won a charger")
    case 5 :
        print("You won a smartphone")
    case 6:
        print("You won a laptop")
    case _ :
        print("Better luck next time")
        
print(" The code is executed succesfully")

for i in range(1,11):
    print("5 x ",i, "=", 5*i)
i=1
while i<11:
    print(i)
    i = i + 1 
for i in range(0,21):
    print(i)
    if i==11:
        break
for i in range(0,20):
   if  i ==10:
        continue # continue the loop for the next iteration here itself so 10 will be skiped
   print(i)
i=3
if i==3:
    pass # pass say that do nothing just skip this and execute the next program
print("End of the program")
name1 = 'Swagatam'
name2 = "Swagatam"
name3 = '''Swagatam is a good
boy. Who lived in kolkata''' # In Triple cote you can use multi line strings and any thing but not for single or double cote
print(name1)
print(name2)
print(name3)
name = 'Swagatam' # name =  'S    w   a   g   a   t   a   m'
print(name[0])    #          0    1   2   3   4   5   6   7
print(name[1])    #         -8    -7  -6  -5  -4  -3  -2  -1
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[-1]) # It will print the last character
Name = 'Swagatam'
print(Name[0:2]) # Goes from 0 to 2-1 i,e, 0 to 1
print(Name[2 : -1]) # Same as name[2:7]
print(Name[0:7:2]) # Skip n-1 chararacter i,e 2-1 = 1 character
print(Name[0:7:3])  # Skip n-1 chararacter i,e 3 - 1 = 2 character
template = "Dear {} . You are a promising guy, take this ₹{} back" # String Formatting.
a = "Swagatam"
a1 = 1000
b = "Anish"
b1 = 10000
c = 'Saptak'
c1 = 1000000000
# s1 = template.format(a,a1)
# print(s1)
# y2 = template.format(b,b1)
# print(y2)
# z3 = template.format(c,c1)
# print(z3)
print(f"{a} you are awasome take this back {a1}$ ") # This is the concept of F-string and how we can apply.
print(f"{b} you are awasome take this back {b1}$ ")
print(f"{c} you are awasome take this back {c1}$ ")
def function(a,b):
    """This is the docstring of the function which explains about the function
    This function takes two numbers as input and returns their sum as output"""
    return a + b;
c = function(5,10)
print(c);
def function2(a,b):
    """This function takes two numbers as input and an optional parameter plus.
    If plus is provided, it adds that to the sum of a and b."""
    x = a + b  ;
    return x;
    c = function2(5,10);
    print(c);
'''Lambda Function
 Lambda functions are small anonymous functions that can take any number of arguments, but can only have one expression.'''
square = lambda x: x * x
'''This is a lambda function example that calculates the square of a number.and we can call it like normal function.
It is as good and compatable writing def square(a): return a * a'''
sum = lambda x, y: x + y
'''This is a lambda function example that calculates the square of a number and another that sums two numbers.and we can call them like normal functions.
It is as good and compatable writing def sum(a,b): return a + b'''
print(square(5))  # Output: 25
print(sum(5, 10))  # Output: 15
'''Recursion in Python
Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller, similar subproblems.'''
'''Fibonacci Series using Recursion.   The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 ...
0 1 2 3 4 5 6  7  8  9 10 11  12  13  14  15  16   17   18   19   20   21
fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0) = 1 + 0 = 1
fib(3) = fib(2) + fib(1) = 1 + 1 = 2
fib(4) = fib(3) + fib(2) = 2 + 1 = 3
fib(5) = fib(4) + fib(3) = 3 + 2 = 5
fib(n) = fib(n-1) + fib(n-2) for n > 1'''

def fib(n):
    # Base case of recursion
    if(n==0 or n==1):
        return n
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))
def sum(a,b):
    """This function takes two numbers as input and returns their sum as output. and a and b are local variables.that means they can only be used inside this function."""
    z = 7 # z is a local variable. that means it can only be used inside this function. It destroyed after the function returns.
    c = a+b
    return c;
Z = 8 # Z is a global variable. that means it can be used anywhere in the program.
print(sum(5,10))
print("The value of global variable Z is :", Z)
def sum(a,b):
        
        c = a+b
        global z # This line tells Python that we want to use the global variable z instead of creating a new local variable z.It says that we are going to use the global variable z inside this function.
        z = 7    # Update the global variable z
        return c;
z =3;
print(sum(5,10))
print("The value of global variable z is :", z)
'''Docstrings in Python
# Docstrings, or documentation strings, are a way to document your Python code. They are used to describe the purpose and functionality of modules, classes, functions, and methods. Docstrings are enclosed in triple quotes ("or") and are placed immediately after the definition of a module, class, function, or method. '''

def sum(a,b):
    """This is the docstring of the function which explains about the function
    This function takes two numbers as input and returns their sum as output"""
    c = a + b;
    return c;
print(sum(5,10))
print(sum.__doc__)  # This will print the docstring of the function sum
squre = lambda x: x * x
list1 = [1,2,3,4,5]
squared_list = list(map(squre, list1)) # map function applies the lambda function to each element of the list1
print(squared_list)
print(list(map(squre, list1)))  # This line is equivalent to the previous one but more explicit. this will also print the squared_list.this is just to show that both are same. This explains how map function works with lambda functions.
def factorial(n):
    """This function takes a number as input and returns its factorial as output using recursion."""
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
def sum_of_digits(n):
    """This function takes a number as input and returns the sum of its digits using recursion."""
    if n==0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)  # n % 10 gives the last digit of n and n // 10 removes the last digit from n
print(sum_of_digits(1234))  # Output: 10 (1 + 2 + 3 + 4 = 10)   
'''Explanation:
The function sum_of_digits takes a number n as input.suppose n = 1234
1. In the first call, n is 1234. It calculates 1234 % 10 = 4 (last digit) and calls sum_of_digits(1234 // 10) = sum_of_digits(123).
2. In the second call, n is 123. It calculates 123 % 10 = 3 (last digit) and calls sum_of_digits(123 // 10) = sum_of_digits(12).
3. In the third call, n is 12. It calculates 12 % 10 = 2 (last digit) and calls sum_of_digits(12 // 10) = sum_of_digits(1).
4. In the fourth call, n is 1. It calculates 1 % 10 = 1 (last digit) and calls sum_of_digits(1 // 10) = sum_of_digits(0).
5. In the fifth call, n is 0. This is the base case, so it returns 0.
Now, the function starts returning values back up the call stack:
# - The fourth call returns 1 + 0 = 1.
# - The third call returns 2 + 1 = 3.   
# - The second call returns 3 + 3 = 6.
# - The first call returns 4 + 6 = 10.
# Thus, the final result is 10, which is the sum of the digits 1, 2, 3, and 4.'''
'''Talking about classes : 
Class is a blue print or a template. E.g: - Form which contains name , age and all stuffs .......'''
class Employee :
    Company = "HP" 
    def get_Salary(self):
        print(self) # self is a reference to the current instance of the class. It is used to access the attributes and methods of the class in python. It is a convention to use self as the name of the first parameter of the method in a class, but you can use any name you want.Self is important here because self is the way to reference theobject of the clas which is being created and we can access the attributes and methods of the class using self. It is a way to tell python that we are referring to the current instance of the class. In this case, when we call get_Salary method using the object shivani, self will refer to shivani and we can access the attributes and methods of the class using self.
        return 100000
'''shivani = Employee() # This is an object of the class Employee. We can create multiple objects of the same class. E.g: - Anish = Employee() , Saptak = Employee() and so on .....
print(shivani.Company) # This will print the value of the class variable Company which is "HP". We can access the class variable using the object of the class.
print(shivani.get_Salary()) # This will call the method get_Salary of the class Employee and print the salary which is 100000. We can access the method of the class using the object of the class.   
Now we will talk about the constructor in python. Constructor is a special method in python which is used to initialize the attributes of the class. It is called when an object of the class is created. The name of the constructor method is __init__. It takes self as the first parameter and other parameters as per the requirement. We can use the constructor to initialize the attributes of the class when we create an object of the class. E.g: -'''
class Employee :
    Company = "HP" 
    def __init__(self, name, salary , age, bond): # This is the constructor of the class Employee. It is called when an object of the class is created. It takes self as the first parameter and other parameters as per the requirement. We can use the constructor to initialize the attributes of the class when we create an object of the class.
        self.name = name # Here we are initializing the instance variable name using the constructor. We can access this variable using the object of the class.
        self.salary = salary # Here we are initializing the instance variable salary using the constructor. We can access this variable using the object of the class.
        self.age = age # Here we are initializing the instance variable age using the constructor. We can access this variable using the object of the class.
        self.bond = bond # Here we are initializing the instance variable bond using the constructor. We can access this variable using the object of the class.
    def get_Salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years");


e1 = Employee("Shivani", 100000, 22, "2 years") # This is an object of the class Employee. We can create multiple objects of the same class. E.g: - Anish = Employee("Anish", 10000, 21, "1 year") , Saptak = Employee("Saptak", 1000000, 25, "5 years") and so on .......
print(e1.name) # This will print the name of the employee which is "Shivani". We can access the instance variable using the object of the class.
print(e1.salary) # This will print the salary of the employee which is 100000. We can access the instance variable using the object of the class.
print(e1.age) # This will print the age of the employee which is 22. We can access the instance variable using the object of the class.
print(e1.bond) # This will print the bond of the employee which is "2 years". We can access the instance variable using the object of the class.
e1.get_info()
''' Difference between class attribute and instance attribute :
Class attribute is a variable that is shared by all the instances of the class. It is defined inside the class but outside                the constructor. It is accessed using the class name or the object of the class. E.g: - Company is a class attribute in the above example. We can access it using Employee.Company or e1.Company.
Instance attribute is a variable that is unique to each instance of the class. It is defined as .....self.variable_name inside the constructor. It is accessed using the object of the class. E.g: - name, salary, age and bond are instance attributes in the above example. We can access them using e1.name, e1.salary, e1.age and e1.bond.'''
class Employee :
    Company = "HP" 
    def __init__(self, name, salary , age, bond, company): # This is the constructor of the class Employee. It is called when an object of the class is created. It takes self as the first parameter and other parameters as per the requirement. We can use the constructor to initialize the attributes of the class when we create an object of the class.
        self.name = name # Here we are initializing the instance variable name using the constructor. We can access this variable using the object of the class.
        self.salary = salary # Here we are initializing the instance variable salary using the constructor. We can access this variable using the object of the class.
        self.age = age # Here we are initializing the instance variable age using the constructor. We can access this variable using the object of the class.
        self.bond = bond # Here we are initializing the instance variable bond using the constructor. We can access this variable using the object of the class.
        self.company = company # Here we are initializing the instance variable company using the constructor. We can access this variable using the object of the class.
    def get_Salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years. Company is {self.company}");
e1 = Employee("Shivani", 100000, 22, "2 years", "Tesla")
print(e1.company) # This will print the company of the employee which is "Tesla". We can access the instance variable using the object of the class. Here, company is an instance variable because it is unique to each instance of the class. It is initialized using the constructor and can be accessed using the object of the class.
print(dir(e1)) # This will print all the attributes and methods of the object e1. We can use this to check whether company is a class attribute or an instance attribute. If it is a class attribute, it will be shared by all the instances of the class and if it is an instance attribute, it will be unique to each instance of the class. In this case, company is an instance attribute because it is unique to each instance of the class. It is initialized using the constructor and can be accessed using the object of the class.
'''Decorators in Python :
Decorator is a functuction that takes a function , it creates a new function inside it's body and returns it. It is used to modify the behavior of a function without changing its code. It is a very powerful tool in python and is widely used in python programming. E.g: - @staticmethod, @classmethod, @property and so on .......
# def decorator_function(original_function):This is a simple example of a decorator function that takes a function as input and returns a new function that adds some functionality to the original function. In this example, the decorator function prints a message before and after the execution of the original function.'''
def decorator(func):
    """
    A decorator function that wraps another function to print messages before and after its execution.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The wrapped function.
    """
    def wrapper():
        print("I am about to execute a function...........")
        func() 
        print("I have executed the function...........")
    return wrapper
@decorator  # This is the syntax for applying a decorator to a function. It is equivalent to say_hello = decorator(say_hello)
def say_hello():
    print("Hello Swagatam !!!")
say_hello() # # This will call the decorated function say_hello which is wrapped by the decorator function. It will print "I am about to execute a function...........", then it will print "Hello Swagatam !!!" and finally it will print "I have executed the function...........". The output will be:
# # I am about to execute a function...........   
f = decorator(say_hello)  # Apply the decorator outside the function
f()  # Call the decorated function
''' we have applied the decorator to the function say_hello using the @decorator syntax. This is a more concise and readable way to apply a decorator to a function. It is equivalent to say_hello = decorator(say_hello) but it is more elegant and easier to understand. The @decorator syntax is widely used in python programming and is considered a best practice for applying decorators to functions.'''
'''Decorators with Arguments :
Decorators can also take arguments. To create a decorator that takes arguments, you need to add an additional layer of nesting to the decorator function. The outer function will take the arguments for the decorator, and the inner function will be the actual decorator that wraps the original function.'''
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
@repeat(7)  # This will repeat the function say_hello 7 times
def say_hello(a):
    print(f"Hello {a} !!!")
say_hello("Swagatam")  # This will call the decorated function say_hello which is wrapped by the decorator function. It will print "Hello Swagatam !!!" 7 times because we have applied the repeat decorator with n=7 to the say_hello function. The output will be:
# Hello Swagatam !!!
'''Now we will learn about property  and setters in python. Property is a built-in function in python that is used to create properties in a class. It is used to define a method as a property. A property is a special kind of attribute that computes its value when accessed. It allows you to define methods that can be accessed like attributes. This is useful for encapsulation and data hiding. Setters are used to set the value of a property. They are defined using the @property decorator and the @<property_name>.setter decorator.'''
class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        l = self.name.split(" ") # This will split the name into a list of words. E.g: - "Shivani Swagatam" will be split into ["Shivani", "Swagatam"]
        return l[0] # This will return the first word of the name which is the first name. E.g: - "Shivani" in the above example.
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ") # This will split the name into a list of words. E.g: - "Shivani Swagatam" will be split into ["Shivani", "Swagatam"]
        new_name = f"{first} {l[1]}" # This will create a new name by replacing the first name with the new first name. E.g: - If we set first_name to "Anish", the new name will be "Anish Swagatam"
        self.name = new_name # This will update the name of the employee with the new name

# Example usage (assuming this is what 'e' was intended for)
e = Employee("Swagatam Chakraborty", 50000)
print(e.first_name)  # Output: Swagatam
e.first_name = "Anish"  # This will change the first name to "Anish" and update the name to "Anish Chakraborty"
print(e.name)  # Output: Anish Chakraborty
