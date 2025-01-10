print("HELLO WORLD")


print("nikhil is my name.","my age is 20.")


print(23+42)


name="nikhil"    # string
age=20
price=25.99
print("my name is:",name)
print("my age is:",age)



print(type(name))
print(type(age))
print(type(price))


name1="nikhil"
name2='nikhil'
name3='''nikhil'''
print(name1)
print(name2)
print(name3)

old=False
print(type(old))

a=None
print(type(a))


a=5
b=3
print("The sum of a and b is :",a+b)


# arithmatic operator
a=5
b=2

print(a+b)    # addition
print(a-b)    # subtraction
print(a*b)    # multiplication
print(a/b)    # division
print(a%b)    # modulus
print(a**b)   # power


# relational operator
x=34
y=35

print(a==b)     # this will return bool value
print(a!=b)     # this will return bool value
print(a<=b)     # this will return bool value
print(a>=b)     # this will return bool value
print(a<b)      # this will return bool value
print(a>b)      # this will return bool value



# assignment operator

num=20
num1=50

 
num+=20
num1-=25
print(num)
print(num1)


# logical operator
val1=True
val2=True


print("and operator:",val1 and val2)
print("or operator:",val1 or val2)
print("not operator:",not val1)  



# type convertion(implicit convertion)
a=2
b=4.33
sum=a+b
print(sum)


# a=("2")#   there is an error because of str is not added with float  
# b=4.25
# sum=a+b
# print(type(a))
# print(sum)

a=int("2")
b=4.25
sum=a+b
print(type(a))
print(sum)

a="2"
a=str(a)
print(type(a))


# taking input
val=input("Enter the value:")
print(type(val))
print("Entered value:",val)


# practice question 1
a=int(input("Enter the frist number:"))
b=int(input("Enter the second number:"))
sum=a+b
print("The sum is:",sum)

# practice question 2
a=int(input("Enter the side of square:"))
area=a*a
print("The area is:",area)


# practice question 3
a=float(input("Enter the frist number:"))
b=float(input("Enter the second number:"))
avg=(a+b)/2
print("The average is:",avg)


# practice question 4
a=int(input("Enter the frist number:"))
b=int(input("Enter the second number:"))
print(a>=b)