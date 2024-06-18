#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q7 : Write a python program that takes a string as input and return its length.
# Ans:
string = input("Enter the String : ")
print(len(string))


# Q8 : Write a python program that concatenates two strings and return the result.
# Ans:
S1= input("Enter the String 1 : ")
S2= input("Enter the String 2 : ")
print(S1+S2)


# Q9 : Write a python program that checks if a substring is present in a given string.
# Ans:
Str1= input("Enter the String : ")
Sub=input("Enter the substring to find : ")
num=Str1.find(Sub)
if num>=0:
    print("Substring is present in the String .")
else:
    print("Substring is not found in the String .")
