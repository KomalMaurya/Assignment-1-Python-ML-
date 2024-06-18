#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q16 : Write a python program that counts the frequency of each character in a string.
# Ans :
string=input("Enter the string : ")
dict1=dict()
count=0
for i in string:
    count=0
    for j in string:
        if i==j:
            count+=1
    dict1[i]=count
print(dict1)


# Q17 : Write a program in python that converts a given string to title case (first letter of each word capitalized).
# Ans :
str1=input("Enter the string : ")
str1=str1.title()
print(str1)


# Q18 : Write a python program that checks if two strings are anagrams of each other.
# Ans :
st1= input("Enter the first String : ")
st2= input("Enter the second String : ")
list1=list(st1)
list2=list(st2)
list1.sort()
list2.sort()
if(list1==list2):
    print("Anagram")
else:
    print("Not Anagram")