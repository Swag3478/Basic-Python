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
