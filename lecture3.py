# list data type
marks=[94.4,87.5,92.4,87,66]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(len(marks))



multi=["Nikhil","Keshari",9621235637,"love",456.643]
print(multi)



# mutability of list which is not in string
str=["nikhil","d","hfw"]
print(str)
str[0]='d'
print(str)



# slicing
marks1=[94.4,87.5,92.4,87,66]
print(len(marks1))
print(marks1[1:3])


print(marks1[3:len(marks1)])
print(marks1[-3:-1])



# list.append()
# add one element at the end
list=[1,2,3,4,5]
list.append(6)
print(list)



# list.sort()
# sorts in assending order
list1=[5,4,3,2,1]
list1.sort()
print(list1)



# list.sort(reverse=True)
# sort in desending order
list2=[1,2,3,4,5]
list2.sort(reverse=True)
print(list2)



# list.reverse()
list3=[1,3,5,7,9]
list3.reverse()
print(list3)



# list.insert(idx,element)
# insert element at index
list4=[1,3,4,5]
list4.insert(1,2)
print(list4)



# list.remove()
# remove frist occurence of element
list5=[1,2,3,4,5,1,2]
list5.remove(1)
print(list5)



# list.pop(idx)
# remove element at index
list6=[1,2,3,4,5,6]
list6.pop(5)
print(list6)



# concatinate
l1=[1,2,3]
l2=[1,2,3]
print(l1+l2)

#=======================================================================================
# tuple
tup=(1,2,3,4,5)
print(type(tup))


# to create a single element tuple
tup1=(1)
print(type(tup1))#this return type='int'

tup2=(1,)
print(type(tup2))#this return type='tuple'

# slicing in tuple
tup3=(1,2,3,4,5,6,7,8)
print(tup3[1:len(tup3):2])

# to return index of frist occurence
# we use tup.index(element)
tup4=(1,2,3,4,4,3,2,1)
print("index of 4:",tup.index(4))

# to count total occurence
# we use tup.count(element)
tup5=(1,2,1,3,4,2,3,4,2,211,1,3,112,32,41,1,32) 
print("total occurence:",tup5.count(1))


# pracice question 1
# wap a progran to ask the user to enter names of thier 3 favorite mvies & store them in a list
list=[]
str=input("Enter the frist movies:")
list.append(str)
str=input("Enter the second movies:")
list.append(str)
str=input("Enter the third movies:")
list.append(str)
print(list)


# practice question
# wap to check if a list is palindrome of element.
# [1,2,3,2,1]                      [1,"abc","abc",1]

list1=[1,2,3,2,1]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome.")
else:
    print("not palindrome.")

# practice question 
# wap to count the number of students with the "A" grsde in the following tuple
# ("D","C","A","A","B","B","A")
tup6=("D","C","A","A","B","B","A")
print("student having grade 'A':",tup6.count("A"))


# practice question 
# store the above values ina list &sort them from "A" to "D"
grade=["D","C","A","A","B","B","A"]
grade.sort()
print(grade)