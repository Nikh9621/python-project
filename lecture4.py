# dictionary and set in python
# dictionary
# syntax
dict={
    "key":"value"
}

# to create a dictionary
info={
    "name":"nikhil",
    "sgpa":"7.77",
    "subject":["physics","evs","pps","electrical","maths"],
    "marks":"(33,45,38,38,52)",
    "age":35,
    "is adult":True
}
# printing dictionary
print(type(info))
print(info["age"])
print(info["sgpa"])
print(info["is adult"])
print(info["marks"])

# mutability
info["sgpa"]="8.5+"
print(info["sgpa"]) 

# we create a null dictionary
null_dict={}
print(null_dict)


# nesting in dictionary
student={
    "name1":"Nikhil Keshari",
    "subject":{
        "phy":33,
        "math":52,
        "pps":38,
        "evs":45,
        "electrical":38
    }
}
print(student["subject"]["math"])


student={
    "name1":"Nikhil Keshari",
    "subject":{
        "phy":33,
        "math":52,
        "pps":38,
        "evs":45,
        "electrical":38
    }
}

print(student.keys())
print(student.values())
print(student.items())
print(list(student))
print(student.get("name1"))
print(student["name1"])
student.update({"sgpa":"7.77"})
print(student)



# *********************************set********************************* #
# syntax
# set is mutable
# set 's element is immutable means element does not change
# inside set we add tuple but does not add list and dictionary
# repeated element is stored ones
# in set hashable value is stored not unhashble value

null_set=set()# empty set syntax
print(null_set)
set1={1,2,3,4,5,3,2,1}
print(type(set1))
print(set1)
print(len(set1))

setset={1,2,3,4,5,"nikhil",4.6,(1,2,3,4)}#list and dictionary is not pass in set
print(setset)



# method of set
# add element in set
collection =set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
print(collection)

# remove element in set
collection.remove(1)
collection.remove(2)
collection.remove(3)
print(collection)

#  empties the set
set2={1,2,3,4,5}
set2.clear()
print(set2)

# remove a ramdom value from set 
set3={1,2,3,4,5}
print(set3.pop()) 
print(set3.pop()) 

# combines the both set values &returns new
# we use set.union(set2)
set5={1,2,3}
set6={4,5,6}
print(set5.union(set6))


# combines thecommon value &returns new
# we use set.intersection(set2)
set7={1,2,3,4,5,6}
set8={2,4,6}
print(set7.intersection(set8)) 


# practice Question 
# store following words in dictionary 
# table :"apiece of furniture","list of fact and figures"
# cat:"asmall animal"

dict100={"table":"a piece of furniture,list of facts & figures"}
print(dict100)
dict200={"cat":"a small animal"}
print(dict200)


# practice question Question
# you are given a list of subjects for students . Assume ane classroom is required for 1 subject.How many classrooms are needed by all students
# "python","java","C++","python","javascript","java","python","java","C++","C"
list100=["python","java","C++","python","javascript","java","python","java","C++","C"]
set300=set(list100)
print(len(set300))


# practice Question
# wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary &add one by one.
# use subject name as key &marksas valve
marks={}
math=int(input("Enter the marks of math "))
marks.update({"maths":math})
phy=int(input("Enter the marks of phy "))
marks.update({"physics":phy})
chem=int(input("Enter the marks of chem "))
marks.update({"chemistry":chem})
print(marks)

