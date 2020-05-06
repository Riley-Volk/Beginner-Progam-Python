print("Hello, World!", end = " ")
print("My name is Riley!\n")
print("I'm learning python coding, \nplease be patient :)")

print()

# this is a single line comment

''' hello 
this is a multiple 
line comment '''

# Variables: no int, double or anything needed
x = 4
t = 1.5
y = "word"
z = "z"
print("x =", x) #no space after '=' sign

# Mathematical operands
w = 3/4
print("w =", w)
i = 3//4
print("i =", i)
# for things to the power
j = 2**3
print("j =", j)
print()

x = input("Enter a number: ")
print("You entered:", x)

# if statements
print("\nIf Statements: ")
if 4 > 5:
    print("4 is less than 5")
elif 4 > 3:
    print("3 is not greater than 4")
else:
    print("1")

# while loops
print("\nwhile loops: ")
x = 0
while x < 5:
    print(x, end = " ")
    x +=1
print("\n\nFor Loops: ")

# for loops
for x in range(5):
    print(x, end = " ")

print("\n\nFor loops starting at 2")
for x in range(2, 10):
    print(x, end = " ")
print("\n\nFor loops starting at 2 and going up by 3")
for x in range(2, 10, 3):
    print(x, end = " ")

print("\n")

# Making classes and objects
class Dog:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        self._age = age

    def __str__(self):
        return "Dog -\nName: " + self._name + "\nAge: " + str(self._age)

dog1 = Dog("Scruffy", 5)
print(dog1)
dog2 = Dog("George", 3)
print(dog2)
