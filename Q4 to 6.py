#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q4 : Write a program that asks the user for their name and then prints a greeting message.
# Ans:
name=input("Enter your name : ")
print("Hello "+name)


# Q5 : Write a program that takes a string input from the user and writes it to a text file.
# Ans:
file_object=open("Text.txt","w+")
Input=input("Enter the String :")
file_object.write(Input)


# Q6 : Write a program that reads the content of a text file and prints it to the console.
# Ans:
file_obj=open("Text.txt","r")
print(file_obj.read())
