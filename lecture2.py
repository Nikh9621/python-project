# string
str1="good morning!"
str2='hi, my name is nikhil.'
str3="""i am from mirzapur."""
# this is the way to write string



str4="this is the string .\nwe are creting in python."
print(str4)
# this is for next line "\n"
str5="this is the string .\twe are creting in python."
print(str5)
# '\t' is used for tab



# concatination
# this is used for adding string
str6="Nikhil"
str7="Keshari"
finalstr=str6+" "+str7
print(finalstr)



# length of str
str8="Nikhil"
print(len(str8))



# slicing
str9="Nikhil Keshari"
print(str9[7:len(str9)])


str10="apple"
print(str10[-5:-2])



# str.endswith()
str11="nikhil"
print(str11.endswith("il"))



# str.capitalize()
str12="nikhil"
str12=str12.capitalize()
print(str12)




# str.casefold()
str12="Nikhil"
str12=str12.casefold()
print(str12)



# str.replace()
str13="Nikhil"
print(str13.replace("i","a"))



# str.find()
str14="This is my python code."
print(str14.find("y"))



# str.count()
str15="i love india."
print(str15.count("i")) 



# practice qyestion 1
name=input("Enter the name:")
print("Length ofname:",len(name))



# practice question 2
str=input("Enter the string:")
print("number of occurence:",str.count("$"))



# conditional statement 
# if-elif-else statement


# code for eligibility criteria for vote
age=int(input("Enter your age:"))
if(age>=18):
    print("You are eligible for vote.")
else:
    print("You are not eligible for vote.")



# trafficlight problem
light=input("Enter the color of light of traffic signal:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("ready")
elif(light=="green"):
    print("go")
else:
    print("invalid light.")


 # grading system
marks=int(input("Enter the marks:"))
if(marks>=90):
    print("Grade:A")
elif(marks<=90 & marks>=80):
    print("Grade:B")
elif(marks<80 & marks>=70):
    print("Grade:C") 
elif(marks<=70):
    print("Grade:D")
else:
    print("Fail")




# practice question 1
# odd even
x=int(input("Enter the number:"))
if(x%2==0):
    print("Even")
else:
    print("Odd")



# practice question 2
# greatest of three
d=int(input("Enter the frist number:"))
e=int(input("Enter the second number:"))
f=int(input("Enter the third number:"))
if(d>e and d>f):
    print("frist number is greater.")
elif(e>f and e>d):
    print("second number is greater.")
else:
    print("third number is greater.")



# practice question 3
# multiple of seven
g=int(input("Enter the number:"))
if(g%7==0):
    print("multiple of seven.")
else:
    print("not multipe of seven.")