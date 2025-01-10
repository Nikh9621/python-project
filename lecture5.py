# while loop
# syntax
# while condition:
#   //code//
count=1
while count<=5:
    print(count,":","hello")
    count+=1

i=1
while i<=100:
    print(i)
    i+=1

i=100
while i>=1:
    print(i)
    i-=1

n=int (input("Enter the number:"))
i=1
while i<=10:
    print(n*i)
    i+=1

i=1
while i<=10:
    print(i*i)
    i+=1

tup=(1,4,9,16,25,36,49,64,81,100)
i=0
x=36
while i<len(tup):
    if(tup[i]==x):
        print(i)
        break
    i+=1


i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1


# for loop
# syntax
# for variable in range(number:number)
#   //code//

tup1=(1,2,3,4,5,6,7,8,9)
for val in tup1:
    print(val)


list=[1,2,3,4,5,6,7,5,4,3,2,1]
for vals in list:
    print(vals)

# here we use optional else in for loop

str="Nikhil Keshari"
for i in str:
    print(i)
else:
    print("End")

for i in range(1,11):
    print(i*i)


# factorial
i=int(input("Enter the number:"))
fact=1
for val in range(1,i+1):
    fact=fact*val
print("factorial of given numbr is :",fact)