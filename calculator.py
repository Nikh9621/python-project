print("************************Calculator***********************")
print("\n")
num1=float(input("Enter the frist number:"))
num2=float(input("Enter the second number:"))
print(" Enter 1 for Addition.""\n","Enter 2 for subtraction.""\n","Enter 3 for multiplication.""\n","Enter 4 for Division.""\n")
print("Please enter your choice between 1 to 4:")
choice=int(input())
if(choice==1):
    print("The addition of",num1,"+",num2,"is",num1+num2)
elif(choice==2):
    print("The subtraction of",num1,"-",num2,"is",num1-num2)
elif(choice==3):
    print("The multiplication of",num1,"*",num2,"is",num1*num2)
elif(choice==4):
    print("The division of",num1,"/",num2,"is",num1/num2)