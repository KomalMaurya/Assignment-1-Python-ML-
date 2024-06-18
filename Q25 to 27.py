#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q25 : Write a python program that copies the content of one text file to another.
# Ans :
with open("text.txt","r") as file:
    file_reader=file.read()
    file_obj=open("Text1.txt","w")
    file_obj.write(file_reader)


# Q26 : Write a program in python that checks if a string starts with a given prefix pr ends with a given suffix.
# Ans :
st=input("Enter the string : ")
prefix=input("Enter the prefix : ")
suffix=input("Enter the suffix : ")

if(st[0:len(prefix)]!=prefix):
    print("String doesn't start with given prefix.")
else:
    print("String starts with given prefix.")

if(st[-len(suffix):]!=suffix):
    print("String doesn't end with given suffix")
else:
    print("String ends with given suffix")


# Q27 : Write a program in python that converts a string into a list of its character.
# Ans :
st=input("Enter the String : ")
list1=[]
for i in st:
    if i not in list1:
        list1.append(i)
print(list1) 