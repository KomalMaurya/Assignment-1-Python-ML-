#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q19 : Write a python program that removes all punctuations from a given string.
# Ans :
string = input("Enter string : ")
new_str=""
for i in string:
    if i.isalnum():
        new_str+=i
print(new_str)


# Q20 : Write a python program that takes a list of numbers and returns their sum.
# Ans :
list1=list(eval(input("Enter the list of numbers : ")))
sum=0
for i in list1:
    sum+=i
print(sum)


# Q21 : Write a python program that counts the occurences of a specific element in a list.
# Ans :
list1=list(eval(input("Enter the list : ")))
print(list1)
dict1=dict()
count=0
for i in list1:
    count=0
    for j in list1:
        if i==j:
            count+=1
    dict1[i]=count
print(dict1)
