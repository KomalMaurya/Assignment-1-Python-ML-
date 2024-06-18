#                                   PYTHON PROGRAMMING ASSIGNMENT - 1

# Q13 : Write a python program that asks user for their birth year and calculate their age.
# Ans :
num=int(input("Enter your birth year : "))
n=int(input("Enter the current year : "))
print(n-num,"is your age!")


# Q14 : Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
#Ans :
string=input("Enter the string : ")
str1=""
while(string!=""):
    str1=str1+string
    string=input("Enter the string : ")
print(str1)


# Q15 : Write a program that reads data from a csv file and prints it to the console.
# Ans :
import csv
with open('CSV_file.csv','r') as csvfile:
    csv_reader=csv.reader(csvfile)
    for row in csv_reader:
        print(row) 